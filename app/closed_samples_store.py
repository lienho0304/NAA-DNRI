import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CLOSED_SAMPLES_FILE = os.path.join(DATA_DIR, "closed_samples.json")


def _ensure_store() -> None:
	os.makedirs(DATA_DIR, exist_ok=True)
	if not os.path.exists(CLOSED_SAMPLES_FILE):
		with open(CLOSED_SAMPLES_FILE, "w", encoding="utf-8") as f:
			json.dump({"next_id": 1, "closed_samples": []}, f, ensure_ascii=False, indent=2)


def _read() -> Dict[str, Any]:
	_ensure_store()
	with open(CLOSED_SAMPLES_FILE, "r", encoding="utf-8") as f:
		return json.load(f)


def _write(data: Dict[str, Any]) -> None:
	with open(CLOSED_SAMPLES_FILE, "w", encoding="utf-8") as f:
		json.dump(data, f, ensure_ascii=False, indent=2)


def list_closed_samples() -> List[Dict[str, Any]]:
	"""Get all closed samples"""
	return _read().get("closed_samples", [])


def create_closed_sample(
	closing_date: str,
	customer_name: str,
	sample_name: str,
	encoding: str,
	box_symbol: str,
	weight: float,
	moisture: float,
	note: str = ""
) -> int:
	"""Create a new closed sample record"""
	data = _read()
	closed_sample_id = data["next_id"]
	
	# Calculate corrected weight (weight - moisture weight)
	moisture_weight = weight * (moisture / 100) if moisture > 0 else 0
	corrected_weight = weight - moisture_weight
	
	closed_sample = {
		"id": closed_sample_id,
		"closing_date": closing_date,
		"customer_name": customer_name,
		"sample_name": sample_name,
		"encoding": encoding,
		"box_symbol": box_symbol,
		"weight": weight,
		"moisture": moisture,
		"corrected_weight": corrected_weight,
		"note": note,
		"created_at": datetime.now().isoformat()
	}
	
	data["closed_samples"].append(closed_sample)
	data["next_id"] += 1
	_write(data)
	
	return closed_sample_id


def create_closed_sample_with_boxes(
	closing_date: str,
	customer_name: str,
	sample_name: str,
	encoding: str,
	boxes: List[Dict[str, Any]],
	note: str = ""
) -> List[int]:
	"""Create multiple closed sample records for the same sample with different boxes"""
	data = _read()
	created_ids = []
	
	for box in boxes:
		closed_sample_id = data["next_id"]
		
		# Calculate corrected weight (weight - moisture weight)
		weight = float(box.get("weight", 0))
		moisture = float(box.get("moisture", 0))
		moisture_weight = weight * (moisture / 100) if moisture > 0 else 0
		corrected_weight = weight - moisture_weight
		
		closed_sample = {
			"id": closed_sample_id,
			"closing_date": closing_date,
			"customer_name": customer_name,
			"sample_name": sample_name,
			"encoding": encoding,
			"box_symbol": box.get("box_symbol", ""),
			"weight": weight,
			"moisture": moisture,
			"corrected_weight": corrected_weight,
			"note": note,
			"created_at": datetime.now().isoformat()
		}
		
		data["closed_samples"].append(closed_sample)
		data["next_id"] += 1
		created_ids.append(closed_sample_id)
	
	_write(data)
	return created_ids


def get_closed_sample(closed_sample_id: int) -> Optional[Dict[str, Any]]:
	"""Get a specific closed sample by ID"""
	closed_samples = list_closed_samples()
	for sample in closed_samples:
		if sample["id"] == closed_sample_id:
			return sample
	return None


def update_closed_sample(
	closed_sample_id: int,
	closing_date: str,
	customer_name: str,
	sample_name: str,
	encoding: str,
	box_symbol: str,
	weight: float,
	moisture: float,
	note: str = ""
) -> bool:
	"""Update an existing closed sample"""
	data = _read()
	for sample in data["closed_samples"]:
		if sample["id"] == closed_sample_id:
			# Calculate corrected weight
			moisture_weight = weight * (moisture / 100) if moisture > 0 else 0
			corrected_weight = weight - moisture_weight
			
			sample["closing_date"] = closing_date
			sample["customer_name"] = customer_name
			sample["sample_name"] = sample_name
			sample["encoding"] = encoding
			sample["box_symbol"] = box_symbol
			sample["weight"] = weight
			sample["moisture"] = moisture
			sample["corrected_weight"] = corrected_weight
			sample["note"] = note
			
			_write(data)
			return True
	return False


def delete_closed_sample(closed_sample_id: int) -> bool:
	"""Delete a closed sample"""
	data = _read()
	data["closed_samples"] = [s for s in data["closed_samples"] if s["id"] != closed_sample_id]
	_write(data)
	return True


def export_closed_samples_to_excel() -> str:
	"""Export closed samples to Excel format"""
	import io
	import pandas as pd
	
	closed_samples = list_closed_samples()
	
	# Create DataFrame
	df = pd.DataFrame(closed_samples)
	
	# Reorder columns for better display
	column_order = [
		"id", "closing_date", "customer_name", "sample_name", "encoding", 
		"box_symbol", "weight", "moisture", "corrected_weight", "note"
	]
	
	# Only include columns that exist in the data
	available_columns = [col for col in column_order if col in df.columns]
	df = df[available_columns]
	
	# Rename columns to Vietnamese
	column_names = {
		"id": "ID",
		"closing_date": "Ngày đóng mẫu",
		"customer_name": "Tên khách hàng",
		"sample_name": "Tên mẫu",
		"encoding": "Mã hóa",
		"box_symbol": "Ký hiệu box",
		"weight": "Khối lượng cân (g)",
		"moisture": "Độ ẩm (%)",
		"corrected_weight": "Khối lượng hiệu chỉnh (g)",
		"note": "Ghi chú"
	}
	
	df = df.rename(columns=column_names)
	
	# Create Excel file in memory
	output = io.BytesIO()
	with pd.ExcelWriter(output, engine='openpyxl') as writer:
		df.to_excel(writer, sheet_name='Mẫu đã đóng', index=False)
	
	output.seek(0)
	return output.getvalue()
