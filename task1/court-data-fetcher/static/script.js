// JavaScript for Court Data Fetcher

document.addEventListener('DOMContentLoaded', function() {
    // Form submission loading state
    const searchForm = document.getElementById('searchForm');
    const submitBtn = document.getElementById('submitBtn');
    
    if (searchForm && submitBtn) {
        searchForm.addEventListener('submit', function(e) {
            // Show loading state
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Searching...';
            submitBtn.disabled = true;
            document.body.classList.add('loading');
            
            // Re-enable after 30 seconds (safety measure)
            setTimeout(function() {
                if (submitBtn.disabled) {
                    submitBtn.innerHTML = '<i class="fas fa-search me-2"></i>Search Case';
                    submitBtn.disabled = false;
                    document.body.classList.remove('loading');
                }
            }, 30000);
        });
    }
    
    // Auto-dismiss alerts after 10 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-warning)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 10000);
    });
    
    // Form validation
    const caseNumberInput = document.getElementById('case_number');
    if (caseNumberInput) {
        caseNumberInput.addEventListener('input', function() {
            const value = this.value;
            // Remove non-numeric characters
            this.value = value.replace(/[^0-9]/g, '');
        });
    }
});

// Utility functions
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(function() {
        const bsAlert = new bootstrap.Alert(alertDiv);
        bsAlert.close();
    }, 5000);
}