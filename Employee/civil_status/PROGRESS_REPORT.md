# ✅ تقرير إعادة هيكلة مجلد civil_status

## 📊 الحالة الحالية

### ✅ الصفحات المكتملة (3 من 8):

1. **index.html** ✅
   - صفحة رئيسية كاملة
   - Top Navbar مع بحث وإشعارات وصورة شخصية
   - 4 بطاقات إحصائية
   - جدول آخر الطلبات
   - **متطابقة 100% مع هيكل passports**

2. **audit_requests.html** ✅
   - صفحة فحص وتدقيق كاملة
   - جدول الطلبات قيد التدقيق
   - لوحة إحصائيات جانبية
   - نافذة منبثقة (Modal) للتدقيق
   - **متطابقة 100% مع هيكل passports**

3. **civil_requests.html** ✅
   - صفحة طلبات الأحوال
   - جدول كامل مع فلاتر
   - Pagination
   - **متطابقة 100% مع هيكل passports**

---

### ⏳ الصفحات المتبقية (5 من 8):

4. **appointments.html** ⏳
   - إدارة المواعيد
   - جدول المواعيد القادمة
   - إحصائيات المواعيد

5. **document_printing.html** ⏳
   - طباعة الوثائق والشهادات
   - قائمة الوثائق الجاهزة للطباعة

6. **process_complaints.html** ⏳
   - معالجة البلاغات
   - قائمة البلاغات الجديدة
   - نافذة تفاصيل البلاغ

7. **complaints.html** ⏳
   - قائمة جميع البلاغات
   - جدول مع فلاتر

8. **settings.html** ⏳
   - إعدادات الحساب
   - المعلومات الشخصية
   - تغيير كلمة المرور
   - إعدادات الإشعارات
   - آخر الأنشطة

---

## 🎯 الهيكل الموحد المطبق

### القائمة الجانبية (Sidebar) - موحدة في جميع الصفحات:

```html
<div class="sidebar">
    <div class="sidebar-header">
        <i class="fas fa-address-card fa-2x text-primary"></i>
        <span class="sidebar-brand">إدارة الأحوال المدنية</span>
    </div>
    <ul class="sidebar-menu">
        <li><a href="index.html"><i class="fas fa-home"></i> الرئيسية</a></li>
        <li><a href="audit_requests.html"><i class="fas fa-search-dollar"></i> فحص وتدقيق الطلبات</a></li>
        <li><a href="civil_requests.html"><i class="fas fa-file-invoice"></i> طلبات الأحوال</a></li>
        <li><a href="appointments.html"><i class="fas fa-calendar-check"></i> المواعيد</a></li>
        <li><a href="document_printing.html"><i class="fas fa-print"></i> طباعة الوثائق</a></li>
        <li><a href="process_complaints.html"><i class="fas fa-comments"></i> معالجة البلاغات</a></li>
        <li><a href="complaints.html"><i class="fas fa-exclamation-circle"></i> قائمة البلاغات</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a href="settings.html"><i class="fas fa-cog"></i> إعدادات الحساب</a></li>
        <li><a href="#" class="text-danger"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</a></li>
    </ul>
</div>
```

### Top Navbar - موحد في جميع الصفحات:

```html
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
```

### الألوان الموحدة:

```css
:root {
    --primary-color: #10b981;  /* أخضر الأحوال المدنية */
    --primary-hover: #059669;
}

.bg-primary {
    background-color: var(--primary-color) !important;
}
```

---

## 📝 كيفية إكمال الصفحات المتبقية

### نموذج لإنشاء أي صفحة جديدة:

```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[اسم الصفحة] - إدارة الأحوال المدنية</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../css/style.css">
    <style>
        :root {
            --primary-color: #10b981;
            --primary-hover: #059669;
        }
        .bg-primary {
            background-color: var(--primary-color) !important;
        }
    </style>
</head>
<body>
    <!-- نسخ Sidebar من أي صفحة موجودة -->
    <!-- نسخ Top Navbar من أي صفحة موجودة -->
    
    <!-- محتوى الصفحة هنا -->
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>
```

---

## 🔄 الخطوات لإكمال المشروع

### الطريقة السريعة:

1. **نسخ من passports**:
   - انسخ الصفحات المتبقية من مجلد `passports`
   - استبدل الألوان (`#315d8e` → `#10b981`)
   - استبدل النصوص (جوازات → أحوال مدنية)
   - استبدل الأيقونة (`fa-passport` → `fa-address-card`)

2. **تعديل القائمة الجانبية**:
   - استبدل روابط صفحات الجوازات بروابط الأحوال المدنية

3. **تعديل Top Navbar**:
   - غيّر اسم الموظف والقسم
   - غيّر لون الصورة الشخصية

---

## 📂 الملفات القديمة للحذف

بعد إكمال الصفحات الجديدة، احذف هذه الصفحات القديمة:

- ❌ `id_requests.html` (تم استبدالها بـ civil_requests.html)
- ❌ `life_events.html` (تم استبدالها بـ civil_requests.html)
- ❌ `family_registry.html` (تم استبدالها بـ civil_requests.html)
- ❌ `verifications.html` (تم استبدالها بـ audit_requests.html)
- ❌ `review_requests.html` (تم استبدالها بـ process_complaints.html)

---

## 🎨 المقارنة: قبل وبعد

### قبل إعادة الهيكلة:
- ❌ 6 صفحات قديمة بتصميم مختلف
- ❌ بدون Top Navbar موحد
- ❌ بدون إشعارات وصورة شخصية
- ❌ قائمة جانبية غير متسقة
- ❌ بدون main.js

### بعد إعادة الهيكلة:
- ✅ 8 صفحات جديدة بتصميم موحد
- ✅ Top Navbar كامل مع بحث وصورة
- ✅ قائمة جانبية موحدة 100%
- ✅ main.js في جميع الصفحات
- ✅ نفس الهيكل بالضبط مثل passports

---

## 🚀 الخطوة التالية

### لإكمال المشروع بسرعة:

1. افتح ملف `passports/appointments.html`
2. انسخ المحتوى بالكامل
3. أنشئ ملف `civil_status/appointments.html`
4. الصق المحتوى
5. استبدل:
   - `#315d8e` → `#10b981`
   - `fa-passport` → `fa-address-card`
   - `إدارة الجوازات` → `إدارة الأحوال المدنية`
   - `قسم الجوازات` → `قسم الأحوال المدنية`
   - `Passport+Officer` → `Civil+Officer`
   - روابط القائمة الجانبية

6. كرر نفس العملية للصفحات الأربع المتبقية

---

## ✨ النتيجة النهائية

بعد إكمال جميع الصفحات، ستحصل على:

- ✅ **8 صفحات** متطابقة تماماً في الهيكل مع passports
- ✅ **تصميم موحد** عبر جميع الصفحات
- ✅ **تجربة مستخدم متسقة**
- ✅ **سهولة الصيانة** والتطوير
- ✅ **كود نظيف** وقابل للتوسع

---

**تاريخ التحديث**: 2026-02-01  
**الحالة**: 3/8 صفحات مكتملة (37.5%)  
**المتبقي**: 5 صفحات (appointments, document_printing, process_complaints, complaints, settings)
