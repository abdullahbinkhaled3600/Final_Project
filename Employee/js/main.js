/**
 * Employee Management System - Interactive Logic & Toast Notifications
 */

document.addEventListener('DOMContentLoaded', function () {
    // 1. Initialize Toast Container
    const toastContainer = document.createElement('div');
    toastContainer.id = 'toast-container';
    toastContainer.className = 'toast-container position-fixed bottom-0 start-0 p-3';
    toastContainer.style.zIndex = '1100';
    document.body.appendChild(toastContainer);

    // 2. Global Toast Function
    window.showToast = function (message, type = 'success') {
        const toastId = 'toast-' + Date.now();
        const icon = type === 'success' ? 'fa-check-circle' : (type === 'danger' ? 'fa-exclamation-circle' : 'fa-info-circle');
        const bgClass = type === 'success' ? 'bg-success' : (type === 'danger' ? 'bg-danger' : 'bg-primary');

        const toastHTML = `
            <div id="${toastId}" class="toast align-items-center text-white ${bgClass} border-0 show" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">
                        <i class="fas ${icon} me-2"></i> ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;

        toastContainer.insertAdjacentHTML('beforeend', toastHTML);
        const toastElement = document.getElementById(toastId);

        // Auto-remove after 3 seconds
        setTimeout(() => {
            toastElement.classList.remove('show');
            setTimeout(() => toastElement.remove(), 500);
        }, 3000);
    };

    // 3. Handle Form Submissions (Demo)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const submitBtn = form.querySelector('[type="submit"]');
            const originalText = submitBtn ? submitBtn.innerHTML : '';

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span> جاري المعالجة...';
            }

            // Simulate API Call
            setTimeout(() => {
                showToast('تمت العملية بنجاح!', 'success');
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }
                form.reset();

                // Close Modals if any
                const modal = bootstrap.Modal.getInstance(form.closest('.modal'));
                if (modal) modal.hide();
            }, 1500);
        });
    });

    // 4. Interactive Buttons (Common Actions)
    document.addEventListener('click', function (e) {
        // Audit Page Actions
        if (e.target.closest('.btn-success') && e.target.closest('#auditModal')) {
            showToast('تم اعتماد الطلب وإرساله للبصمة بنجاح', 'success');
            bootstrap.Modal.getInstance(document.getElementById('auditModal')).hide();
        }

        if (e.target.closest('.btn-danger') && e.target.closest('#auditModal')) {
            showToast('تم رفض الطلب بنجاح', 'danger');
            bootstrap.Modal.getInstance(document.getElementById('auditModal')).hide();
        }

        if (e.target.closest('.btn-warning') && e.target.closest('#auditModal')) {
            showToast('تمت إعادة الطلب للاستكمال', 'info');
            bootstrap.Modal.getInstance(document.getElementById('auditModal')).hide();
        }

        // Compliant Page Actions
        if (e.target.closest('.complaint-item')) {
            document.querySelectorAll('.complaint-item').forEach(item => item.classList.remove('active'));
            e.target.closest('.complaint-item').classList.add('active');
            showToast('تم تحميل بيانات البلاغ', 'info');
        }

        if (e.target.closest('.btn-primary-custom') && e.target.closest('.main-content') && e.target.innerText.includes('إرسال الرد')) {
            showToast('تم إرسال الرد للمواطن بنجاح', 'success');
            const textarea = document.querySelector('textarea');
            if (textarea) textarea.value = '';
        }

        // Generic "Process" buttons in tables
        if (e.target.classList.contains('btn-primary-custom') && !e.target.closest('.modal') && !e.target.closest('.sidebar')) {
            if (!e.target.dataset.bsToggle) { // Not a modal toggle
                const buttonText = e.target.innerText || e.target.textContent;

                // Navigate to audit page if button says "تدقيق"
                if (buttonText.includes('تدقيق')) {
                    showToast('جاري الانتقال إلى صفحة التدقيق...', 'info');
                    setTimeout(() => {
                        window.location.href = 'audit_requests.html';
                    }, 800);
                }
                // Navigate to complaints page if button says "معالجة"
                else if (buttonText.includes('معالجة')) {
                    showToast('جاري الانتقال إلى صفحة معالجة البلاغات...', 'info');
                    setTimeout(() => {
                        window.location.href = 'process_complaints.html';
                    }, 800);
                }
                else {
                    showToast('جاري البدء في المعالجة...', 'info');
                }
            }
        }
    });

    // 5. Dynamic Sidebar Activity
    const currentPath = window.location.pathname.split('/').pop();
    document.querySelectorAll('.sidebar-menu a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
