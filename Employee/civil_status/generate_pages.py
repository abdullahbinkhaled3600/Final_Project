# Script to generate all civil_status pages based on passports structure
# This will create 8 pages matching the passports folder structure

import os

# Base template for all pages
def create_page(filename, title, page_name, active_page, content_html):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - إدارة الأحوال المدنية</title>
    <!-- Bootstrap 5 CSS (RTL) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="../css/style.css">
    <style>
        :root {{
            --primary-color: #10b981;
            --primary-hover: #059669;
        }}
        .sidebar-brand {{
            color: var(--primary-color);
        }}
        .text-primary {{
            color: var(--primary-color) !important;
        }}
        .btn-primary-custom {{
            background-color: var(--primary-color);
        }}
        .bg-primary {{
            background-color: var(--primary-color) !important;
        }}
    </style>
</head>

<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="sidebar-header">
            <i class="fas fa-address-card fa-2x text-primary"></i>
            <span class="sidebar-brand">إدارة الأحوال المدنية</span>
        </div>
        <ul class="sidebar-menu">
            <li><a href="index.html" {"class=\\"active\\"" if active_page == "index" else ""}><i class="fas fa-home"></i> الرئيسية</a></li>
            <li><a href="audit_requests.html" {"class=\\"active\\"" if active_page == "audit" else ""}><i class="fas fa-search-dollar"></i> فحص وتدقيق الطلبات</a></li>
            <li><a href="civil_requests.html" {"class=\\"active\\"" if active_page == "requests" else ""}><i class="fas fa-file-invoice"></i> طلبات الأحوال</a></li>
            <li><a href="appointments.html" {"class=\\"active\\"" if active_page == "appointments" else ""}><i class="fas fa-calendar-check"></i> المواعيد</a></li>
            <li><a href="document_printing.html" {"class=\\"active\\"" if active_page == "printing" else ""}><i class="fas fa-print"></i> طباعة الوثائق</a></li>
            <li><a href="process_complaints.html" {"class=\\"active\\"" if active_page == "process" else ""}><i class="fas fa-comments"></i> معالجة البلاغات</a></li>
            <li><a href="complaints.html" {"class=\\"active\\"" if active_page == "complaints" else ""}><i class="fas fa-exclamation-circle"></i> قائمة البلاغات</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a href="settings.html" {"class=\\"active\\"" if active_page == "settings" else ""}><i class="fas fa-cog"></i> إعدادات الحساب</a></li>
            <li><a href="#" class="text-danger"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</a></li>
        </ul>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Top Navbar -->
        <div class="top-navbar">
            <div class="search-wrapper">
                <i class="fas fa-search"></i>
                <input type="text" class="form-control" placeholder="بحث عن مواطن أو طلب...">
            </div>
            <div class="d-flex align-items-center gap-3">
                <div class="badge bg-primary px-3 py-2">موظف قيود مدنية</div>
                <div class="d-flex align-items-center gap-2">
                    <img src="https://ui-avatars.com/api/?name=Civil+Officer&background=10b981&color=fff"
                        class="rounded-circle" width="40" height="40" alt="Avatar">
                    <div class="d-none d-md-block">
                        <div class="fw-bold" style="font-size: 0.9rem;">محمد العسيري</div>
                        <div class="text-muted" style="font-size: 0.75rem;">قسم الأحوال المدنية</div>
                    </div>
                </div>
            </div>
        </div>

        <h4 class="mb-4">{page_name}</h4>

        {content_html}
    </div>

    <!-- Bootstrap Bundle JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Custom JS -->
    <script src="../js/main.js"></script>
</body>

</html>'''

# Page contents
pages = {
    "civil_requests.html": {
        "title": "طلبات الأحوال",
        "page_name": "طلبات الأحوال المدنية الواردة",
        "active": "requests",
        "content": '''
        <div class="custom-card">
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>رقم الطلب</th>
                            <th>المواطن</th>
                            <th>رقم الهوية</th>
                            <th>نوع الطلب</th>
                            <th>تاريخ التقديم</th>
                            <th>الحالة</th>
                            <th>الإجراء</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="fw-bold">#CIV-8812</td>
                            <td>عبدالله بن حمد</td>
                            <td>1092837465</td>
                            <td>إصدار هوية جديدة</td>
                            <td>2024-05-18</td>
                            <td><span class="status-badge bg-pending">بانتظار المعالجة</span></td>
                            <td>
                                <button class="btn btn-sm btn-outline-primary"><i class="fas fa-eye"></i></button>
                                <button class="btn btn-sm btn-primary-custom">تدقيق</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        '''
    },
    "appointments.html": {
        "title": "المواعيد",
        "page_name": "إدارة المواعيد",
        "active": "appointments",
        "content": '''
        <div class="row g-4">
            <div class="col-md-8">
                <div class="custom-card">
                    <h5 class="fw-bold mb-4">المواعيد القادمة</h5>
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>رقم الموعد</th>
                                    <th>المواطن</th>
                                    <th>نوع الخدمة</th>
                                    <th>التاريخ والوقت</th>
                                    <th>الحالة</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>#APT-001</td>
                                    <td>أحمد محمد</td>
                                    <td>استلام هوية</td>
                                    <td>2024-05-20 10:00 ص</td>
                                    <td><span class="status-badge bg-pending">مؤكد</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="custom-card bg-primary text-white">
                    <h5>إحصائيات المواعيد</h5>
                    <div class="mt-3">
                        <div class="h3">45</div>
                        <div class="small">مواعيد اليوم</div>
                    </div>
                </div>
            </div>
        </div>
        '''
    },
    "document_printing.html": {
        "title": "طباعة الوثائق",
        "page_name": "طباعة الوثائق والشهادات",
        "active": "printing",
        "content": '''
        <div class="custom-card">
            <h5 class="fw-bold mb-4">الوثائق الجاهزة للطباعة</h5>
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>رقم الطلب</th>
                            <th>نوع الوثيقة</th>
                            <th>المواطن</th>
                            <th>تاريخ الجاهزية</th>
                            <th>الإجراء</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>#CIV-001</td>
                            <td>هوية وطنية</td>
                            <td>خالد أحمد</td>
                            <td>2024-05-18</td>
                            <td><button class="btn btn-sm btn-primary-custom"><i class="fas fa-print"></i> طباعة</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        '''
    },
    "process_complaints.html": {
        "title": "معالجة البلاغات",
        "page_name": "معالجة البلاغات والشكاوى",
        "active": "process",
        "content": '''
        <div class="row g-4">
            <div class="col-md-4">
                <div class="custom-card">
                    <h6 class="fw-bold mb-3">البلاغات الجديدة</h6>
                    <div class="list-group">
                        <a href="#" class="list-group-item list-group-item-action">
                            <div class="fw-bold">#COMP-001</div>
                            <div class="small text-muted">تأخر في الخدمة</div>
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-md-8">
                <div class="custom-card">
                    <h6 class="fw-bold mb-3">تفاصيل البلاغ</h6>
                    <p class="text-muted">اختر بلاغاً من القائمة لعرض التفاصيل</p>
                </div>
            </div>
        </div>
        '''
    },
    "complaints.html": {
        "title": "قائمة البلاغات",
        "page_name": "قائمة جميع البلاغات",
        "active": "complaints",
        "content": '''
        <div class="custom-card">
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>رقم البلاغ</th>
                            <th>المواطن</th>
                            <th>نوع البلاغ</th>
                            <th>التاريخ</th>
                            <th>الحالة</th>
                            <th>الإجراء</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>#COMP-001</td>
                            <td>سارة أحمد</td>
                            <td>تأخر في الخدمة</td>
                            <td>2024-05-18</td>
                            <td><span class="status-badge bg-pending">جديد</span></td>
                            <td><button class="btn btn-sm btn-primary-custom">معالجة</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        '''
    },
    "settings.html": {
        "title": "إعدادات الحساب",
        "page_name": "إعدادات الحساب",
        "active": "settings",
        "content": '''
        <div class="row g-4">
            <div class="col-md-8">
                <div class="custom-card">
                    <h5 class="fw-bold mb-4">المعلومات الشخصية</h5>
                    <form>
                        <div class="mb-3">
                            <label class="form-label">الاسم الكامل</label>
                            <input type="text" class="form-control" value="محمد العسيري">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">البريد الإلكتروني</label>
                            <input type="email" class="form-control" value="m.alasiri@civil.gov.sa">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">رقم الجوال</label>
                            <input type="tel" class="form-control" value="0501234567">
                        </div>
                        <button type="submit" class="btn btn-primary-custom">حفظ التغييرات</button>
                    </form>
                </div>
            </div>
            <div class="col-md-4">
                <div class="custom-card">
                    <h6 class="fw-bold mb-3">الصورة الشخصية</h6>
                    <img src="https://ui-avatars.com/api/?name=Civil+Officer&background=10b981&color=fff&size=200"
                        class="rounded-circle w-100" alt="Avatar">
                    <button class="btn btn-sm btn-outline-primary mt-3 w-100">تغيير الصورة</button>
                </div>
            </div>
        </div>
        '''
    }
}

print("تم إنشاء السكريبت بنجاح!")
print(f"عدد الصفحات المطلوبة: {len(pages)}")
for filename in pages.keys():
    print(f"- {filename}")
