/**
 * Main JavaScript for Manager System
 * Handles Toasts, Sidebar Taggling, and General Interactions
 */

document.addEventListener('DOMContentLoaded', function () {
    // 1. Inject Toast Container
    const toastContainer = document.createElement('div');
    toastContainer.className = 'toast-container position-fixed bottom-0 start-0 p-3';
    toastContainer.style.zIndex = '1100';
    toastContainer.id = 'toastContainer';
    document.body.appendChild(toastContainer);

    // 2. Add Sidebar Toggle Button to Navbar if not exists
    const topNavbar = document.querySelector('.top-navbar');
    if (topNavbar && !document.querySelector('#sidebarToggle')) {
        const toggleBtn = document.createElement('button');
        toggleBtn.id = 'sidebarToggle';
        toggleBtn.className = 'btn btn-light d-md-none me-2'; // Visible only on small screens
        toggleBtn.innerHTML = '<i class="fa-solid fa-bars"></i>';
        topNavbar.prepend(toggleBtn);

        // Sidebar Toggle Logic
        toggleBtn.addEventListener('click', function () {
            document.querySelector('.sidebar').classList.toggle('show');
            document.querySelector('.main-content').classList.toggle('shifted');
        });
    }

    // 3. Global Event Delegation for Buttons (Mock Actions)
    document.body.addEventListener('click', function (e) {
        const target = e.target.closest('button');
        if (!target) return;

        // Ignore buttons that trigger modals or specific navigation
        if (target.hasAttribute('data-bs-toggle') || target.hasAttribute('data-bs-dismiss')) return;

        // Identify action buttons
        if (target.classList.contains('btn-approve') || target.innerText.includes('موافقة') || target.innerText.includes('اعتماد')) {
            showToast('تمت الموافقة على الطلب بنجاح', 'success');
        } else if (target.classList.contains('btn-reject') || target.innerText.includes('رفض')) {
            showToast('تم رفض الطلب', 'danger');
        } else if (target.innerText.includes('حفظ') || target.innerText.includes('إرسال')) {
            // Let the modal close/form submit proceed, but show toast
            // For demo purposes, we delay slightly
            setTimeout(() => showToast('تم حفظ البيانات بنجاح', 'success'), 300);
        } else if (target.classList.contains('text-danger') && target.querySelector('.fa-trash')) {
            if (confirm('هل أنت متأكد من الحذف؟')) {
                showToast('تم الحذف بنجاح', 'success');
            }
        }
    });

    // 4. Initialize Bootstrap Tooltips (if any)
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

/**
 * Show Toast Notification
 * @param {string} message - The message to display
 * @param {string} type - 'success', 'danger', 'warning', 'info'
 */
function showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');

    // Choose icon based on type
    let icon = 'fa-check-circle';
    if (type === 'danger') icon = 'fa-circle-xmark';
    if (type === 'warning') icon = 'fa-triangle-exclamation';

    const toastHTML = `
        <div class="toast align-items-center text-white bg-${type} border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fa-solid ${icon} me-2"></i>
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    `;

    // Create element
    const toastEl = document.createElement('div');
    toastEl.innerHTML = toastHTML;
    const toastNode = toastEl.firstElementChild;

    container.appendChild(toastNode);

    // Init Bootstrap Toast
    const toast = new bootstrap.Toast(toastNode, { delay: 3000 });
    toast.show();

    // Remove after hide
    toastNode.addEventListener('hidden.bs.toast', () => {
        toastNode.remove();
    });
}
