// Lab Sample Management System - Static Version
// Main JavaScript file for static functionality

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Lab Sample Management System - Static Version loaded');
    
    // Initialize any global functionality here
    initializeApp();
});

function initializeApp() {
    // Set up any global event listeners or initialization
    console.log('App initialized');
}

// Utility functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('vi-VN');
}

function formatNumber(number, decimals = 2) {
    return parseFloat(number).toFixed(decimals);
}

// Local Storage helpers
function saveToStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (error) {
        console.error('Error saving to localStorage:', error);
        return false;
    }
}

function loadFromStorage(key, defaultValue = []) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : defaultValue;
    } catch (error) {
        console.error('Error loading from localStorage:', error);
        return defaultValue;
    }
}

// Export functions for CSV/Excel
function exportToCSV(data, filename, headers) {
    if (!data || data.length === 0) {
        alert('Không có dữ liệu để xuất!');
        return;
    }
    
    const csvContent = [
        headers.join(','),
        ...data.map(row => headers.map(header => {
            const value = row[header.toLowerCase().replace(/\s+/g, '_')] || '';
            return `"${value}"`;
        }).join(','))
    ].join('\n');
    
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Form validation helpers
function validateForm(formElement) {
    const requiredFields = formElement.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Show notification
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 5000);
}

// Global error handler
window.addEventListener('error', function(e) {
    console.error('Global error:', e.error);
    showNotification('Đã xảy ra lỗi. Vui lòng thử lại.', 'danger');
});

// Prevent form submission if validation fails
document.addEventListener('submit', function(e) {
    const form = e.target;
    if (form.tagName === 'FORM' && !validateForm(form)) {
        e.preventDefault();
        showNotification('Vui lòng điền đầy đủ thông tin bắt buộc.', 'warning');
    }
});
