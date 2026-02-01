import os
import re

files_to_update = [
    'profile.html', 'edit_profile.html', 'services.html', 
    'my_requests.html', 'booking.html', 'notifications.html', 'complaints.html', 
    'request_details.html', 'service_request.html', 'national_id.html', 
    'birth_certificate.html', 'death_certificate.html', 'spinsterhood_cert.html', 
    'passport_ordinary.html', 'passport_marine.html', 'passport_business.html', 
    'payment.html', 'family_register.html'
]

header_content = """            <div class="d-flex align-items-center gap-3">
                <div class="dropdown">
                    <button class="btn btn-light position-relative rounded-circle" type="button"
                        data-bs-toggle="dropdown">
                        <i class="fas fa-bell text-muted"></i>
                        <span
                            class="position-absolute top-0 start-100 translate-middle p-1 bg-danger border border-light rounded-circle"></span>
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end p-2" style="width: 300px;">
                        <li>
                            <h6 class="dropdown-header">آخر الإشعارات</h6>
                        </li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <!-- Notification Item -->
                        <li>
                            <a class="dropdown-item d-flex gap-2 align-items-start" href="#">
                                <div class="text-primary"><i class="fas fa-check-circle"></i></div>
                                <div>
                                    <small class="d-block text-wrap">تم الموافقة على طلب تجديد الهوية</small>
                                    <small class="text-muted" style="font-size: 0.7rem;">منذ 2 ساعة</small>
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="dropdown">
                    <button class="btn p-0 border-0" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <img src="https://ui-avatars.com/api/?name=User+Name&background=5e6ad2&color=fff" class="rounded-circle"
                            width="40" height="40" alt="User">
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li><a class="dropdown-item" href="profile.html">الإعدادات</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item text-danger" href="index.html">تسجيل خروج</a></li>
                    </ul>
                </div>
            </div>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Sidebar: Profile -> Settings
    # Only if "الإعدادات" is not present to avoid double replacement if run multiple times
    if 'الإعدادات' not in content:
        content = re.sub(
            r'<li><a href="profile\.html"(.*?)><i class="fas fa-user"></i> الملف الشخصي</a></li>', 
            r'<li><a href="profile.html"\1><i class="fas fa-cog"></i> الإعدادات</a></li>', 
            content
        )

    # 2. Update Header: Add Dropdowns
    # Look for the header row
    header_pattern = r'(<div class="d-flex justify-content-between align-items-center mb-4">\s*<div class="d-flex align-items-center">\s*<i class="fas fa-bars menu-toggle me-3" onclick="toggleSidebar\(\)"></i>\s*<h4 class="m-0 fw-bold">.*?</h4>\s*</div>)'
    
    # Check if dropdown already exists in that specific block to avoid duplication
    # We will search for the header block and see if it is followed by our new content
    match = re.search(header_pattern, content)
    if match:
        header_start_block = match.group(1)
        # Check what follows immediately
        post_header_content = content[match.end():]
        # Allow some whitespace
        if 'data-bs-toggle="dropdown"' not in post_header_content[:500]: # simplistic check
            # Look for where the header div ends. The header div is d-flex justify-content-between...
            # The regex captured the inner div. So we are inside the outer div.
            # We just need to insert AFTER the captured group 1.
            # BUT, we need to make sure we don't leave old content (like old images or simple logout buttons if any)
            # Actually, most files have just empty space or a simple image. 
            # To be safe, let's assume we want to replace everything after the title div until the closing div of the header row.
            
            # Since HTML parsing with regex is fragile, and we know the structure is simple:
            # We will replace the whole header row block if we can find the closing div properly.
            # Or simpler: Just insert it after Group 1, and hope there isn't garbage after it.
            # Looking at profile.html, it closes immediately: </div> -> closes header row
            
            # Let's try to replace `header_start_block` + `\s*</div>` with `header_start_block` + `\n` + `header_content` + `\n</div>`
            
            # Better regex: match the whole header container if possible? No, title varies.
            
            # Let's go with insertion.
            replacement = header_start_block + '\n' + header_content
            content = content.replace(header_start_block, replacement)

    # 3. Clean up potential duplicate closing divs if the previous content was just closing div
    # If the original was `...</div> </div>` and we replaced `...</div>` with `...</div> CONTENT`, we are fine.
    
    # Wait, in profile.html:
    # <div class="d-flex justify-content-between ...">
    #    <div class="d-flex ...">...</div>   <-- header_start_block captures this
    # </div>
    #
    # If I replace header_start_block with header_start_block + content
    # Result:
    # <div class="d-flex justify-content-between ...">
    #    <div class="d-flex ...">...</div>
    #    CONTENT
    # </div>
    # This is correct valid HTML structure for flexween between.
    
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for filename in files_to_update:
    path = os.path.join(r'd:\Final_Project\Citizen', filename)
    if os.path.exists(path):
        update_file(path)
    else:
        print(f"File not found: {path}")
