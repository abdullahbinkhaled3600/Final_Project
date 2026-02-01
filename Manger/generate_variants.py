import os

base_dir = "d:\\Final_Project\\Manger"
files_to_process = ["approvals.html", "users.html", "services.html", "reports.html"]

variants = [
    {
        "prefix": "civil",
        "style": "civil_style.css",
        "dashboard": "civil_dashboard.html",
        "title": "مدير الأحوال",
        "remove_branch_sidebar": True
    },
    {
        "prefix": "passport",
        "style": "passport_style.css",
        "dashboard": "passport_dashboard.html",
        "title": "مدير الجوازات",
        "remove_branch_sidebar": True
    }
]

def process_file(filename, variant):
    with open(os.path.join(base_dir, filename), "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Style
    content = content.replace("css/style.css", f"css/{variant['style']}")
    
    # Replace Sidebar Links and Filenames
    content = content.replace("dashboard.html", variant['dashboard'])
    content = content.replace("approvals.html", f"{variant['prefix']}_approvals.html")
    content = content.replace("users.html", f"{variant['prefix']}_users.html")
    content = content.replace("services.html", f"{variant['prefix']}_services.html")
    content = content.replace("reports.html", f"{variant['prefix']}_reports.html")
    
    # Remove Branches Link from Sidebar
    if variant['remove_branch_sidebar']:
        # This acts on the specific line format in the files
        content = content.replace('<li><a href="branches.html"><i class="fa-solid fa-building"></i> إدارة الفروع</a></li>', '')
        # Also clean up empty lines if any created might be handled by browser, but better to be clean.
        # Simple string replace is fine.

    # Replace Title "System Manager"
    content = content.replace("نظام المدير", variant['title'])

    # Replace "Branch" with "Section" in text
    content = content.replace("الفرع", "القسم")
    content = content.replace("فرع", "قسم")
    content = content.replace("branches.html", "#") # In case any remain in body
    
    # Save new file
    new_filename = f"{variant['prefix']}_{filename}"
    with open(os.path.join(base_dir, new_filename), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {new_filename}")

for filename in files_to_process:
    for variant in variants:
        process_file(filename, variant)
