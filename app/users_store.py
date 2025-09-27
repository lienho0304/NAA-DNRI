import json
import os
from typing import Dict, Any, List, Optional
from werkzeug.security import generate_password_hash, check_password_hash


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
USERS_FILE = os.path.join(DATA_DIR, "users.json")


DEFAULT_SECTIONS = [
	"users",
	"customers",
	"receiving",
	"closing",
	"irradiation",
]


def _ensure_store() -> None:
	os.makedirs(DATA_DIR, exist_ok=True)
	if not os.path.exists(USERS_FILE):
		seed_admin()


def seed_admin() -> None:
	"""Create the initial Admin user if file does not exist."""
	os.makedirs(DATA_DIR, exist_ok=True)
	admin_record = {
		"username": "Admin",
		"password_hash": generate_password_hash("admin"),
		"role": "admin",
		"permissions": DEFAULT_SECTIONS,
		"active": True,
	}
	with open(USERS_FILE, "w", encoding="utf-8") as f:
		json.dump({"users": [admin_record]}, f, ensure_ascii=False, indent=2)


def load_users() -> List[Dict[str, Any]]:
	_ensure_store()
	with open(USERS_FILE, "r", encoding="utf-8") as f:
		data = json.load(f)
	return data.get("users", [])


def save_users(users: List[Dict[str, Any]]) -> None:
	os.makedirs(DATA_DIR, exist_ok=True)
	with open(USERS_FILE, "w", encoding="utf-8") as f:
		json.dump({"users": users}, f, ensure_ascii=False, indent=2)


def get_user(username: str) -> Optional[Dict[str, Any]]:
	for user in load_users():
		if user.get("username") == username:
			return user
	return None


def create_user(username: str, password: str, role: str, permissions: List[str]) -> bool:
	username = username.strip()
	if not username or get_user(username):
		return False
	user = {
		"username": username,
		"password_hash": generate_password_hash(password),
		"role": role,
		"permissions": permissions,
		"active": True,
	}
	users = load_users()
	users.append(user)
	save_users(users)
	return True


def delete_user(username: str) -> bool:
	if username == "Admin":
		return False
	users = load_users()
	new_users = [u for u in users if u.get("username") != username]
	if len(new_users) == len(users):
		return False
	save_users(new_users)
	return True


def verify_user_credentials(username: str, password: str) -> bool:
	user = get_user(username)
	if not user or not user.get("active"):
		return False
	return check_password_hash(user.get("password_hash", ""), password)


def is_admin(username: str) -> bool:
	if username == "Admin":
		return True
	user = get_user(username)
	return bool(user and user.get("role") == "admin")


def has_permission(username: str, section: str) -> bool:
	if is_admin(username):
		return True
	user = get_user(username)
	if not user or not user.get("active"):
		return False
	return section in (user.get("permissions") or [])
