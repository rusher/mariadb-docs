import os
import re
import urllib.request

# --- Robust Path Configuration ---
def find_repo_root():
    """Automatically locates the true root of the repository"""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir): 
        if os.path.exists(os.path.join(current_dir, 'server', 'SUMMARY.md')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return os.getcwd() 

DOCS_ROOT = find_repo_root()
SUMMARY_FILE = os.path.join(DOCS_ROOT, 'server', 'SUMMARY.md')
ERROR_CODES_DIR = os.path.join(DOCS_ROOT, 'server', 'reference', 'error-codes')

# The live source of truth from the MariaDB server repository
ERRMSG_URL = 'https://raw.githubusercontent.com/MariaDB/server/refs/heads/main/sql/share/errmsg-utf8.txt'

# --- Regex Patterns ---
ERROR_DEF_RE = re.compile(r'^(ER_|WARN_)([A-Z0-9_]+)\s*([A-Z0-9]+)?\s*([A-Z0-9]+)?')
ENG_TEXT_RE = re.compile(r'^\s+eng\s+"(.*)"')
SUMMARY_SECTION_RE = re.compile(r'^\s*\*\s*\[.*(\d{4})\s+to\s+(\d{4})\].*')

# --- Markdown Template ---
MD_TEMPLATE = """# Error {error_code}: {desc_title}

| Error Code | SQLSTATE | Error                    | Description                                               |
| ---------- | -------- | ------------------------ | --------------------------------------------------------- |
| {error_code:<10} | {sqlstate:<8} | {error_name_escaped:<24} | {description} |

## Possible Causes and Solutions

{custom_content}{{% include "../../../.gitbook/includes/contributing-content.md" %}}

{{% include "../../../.gitbook/includes/license-cc-by-sa-gnu-fdl.md" %}}

{{% @marketo/form formId="4316" %}}
"""

def parse_errmsg_file(url):
    """Downloads and parses the live source txt file."""
    errors = {}
    current_number = 0
    current_obj = None

    print(f"[INFO] Downloading source file from {url}...")
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8', errors='replace')
            lines = content.splitlines()
    except Exception as e:
        print(f"[ERROR] Failed to fetch the file: {e}")
        return {}

    for line in lines:
        line = line.rstrip()
        
        if line.startswith('start-error-number'):
            current_number = int(line.split()[1])
            continue
        if line.startswith('skip-to-error-number'):
            current_number = int(line.split()[1])
            continue

        if line.startswith('ER_') or line.startswith('WARN_'):
            match = ERROR_DEF_RE.match(line)
            if match:
                sqlstate = "HY000" 
                tokens = line.split()
                if len(tokens) > 1 and not tokens[1].startswith('eng'):
                     if len(tokens[1]) == 5:
                         sqlstate = tokens[1]
                
                error_name = tokens[0]

                current_obj = {
                    'code': current_number,
                    'name': error_name,
                    'sqlstate': sqlstate,
                    'description': "" 
                }
                errors[current_number] = current_obj
                current_number += 1
                continue

        if current_obj and 'eng "' in line:
            match = ENG_TEXT_RE.search(line)
            if match:
                current_obj['description'] = match.group(1)
                current_obj = None 

    return errors

def get_folder_name(code):
    return f"mariadb-error-codes-{(code // 100) * 100}-to-{(code // 100) * 100 + 99}"

def preserve_custom_content(file_path):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'## Possible Causes and Solutions\s*\n(.*?)(\n{% include|$)', re.DOTALL)
    match = pattern.search(content)
    if match:
        custom_text = match.group(1).strip()
        if custom_text:
            return custom_text + "\n\n"
    return ""

def update_summary_file(new_pages):
    if not os.path.exists(SUMMARY_FILE):
        return

    with open(SUMMARY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    pages_by_range = {}
    for code, path, title in new_pages:
        range_start = (code // 100) * 100
        pages_by_range.setdefault(range_start, []).append((code, path, title))

    for line in lines:
        new_lines.append(line)
        match = SUMMARY_SECTION_RE.match(line)
        if match:
            range_start = int(match.group(1))
            if range_start in pages_by_range:
                # --- FIX: Match the exact indentation of the folder heading ---
                indent_match = re.match(r'^(\s*)\*', line)
                base_indent = indent_match.group(1) if indent_match else "  "
                # Add exactly two spaces to perfectly nest the page inside the folder
                child_indent = base_indent + "  " 
                
                for code, path, title in pages_by_range[range_start]:
                    path_check = f"/{os.path.basename(path)}"
                    if not any(path_check in l for l in lines):
                        new_lines.append(f"{child_indent}* [{title}]({path})\n")

    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    print("=" * 70)
    print(" DOCS-5990: MariaDB Error Code Automation (GitHub Actions) ")
    print(f" Detected Repository Root: {DOCS_ROOT}")
    print("=" * 70)
    
    errors = parse_errmsg_file(ERRMSG_URL)
    if not errors:
        return
    
    new_pages_for_summary = []

    for code, data in errors.items():
        folder = get_folder_name(code)
        filename = f"e{code}.md"
        
        abs_folder = os.path.join(ERROR_CODES_DIR, folder)
        abs_filepath = os.path.join(abs_folder, filename)
        
        is_unused = data['name'].startswith("ER_UNUSED_")
        file_exists = os.path.exists(abs_filepath)

        if is_unused and not file_exists:
            continue
        elif is_unused and file_exists:
            print(f"[ACTION] OVERWRITE: Error {code} downgraded to unused.")
        elif file_exists:
            continue
        else:
            print(f"[ACTION] CREATE: Missing documentation for Error {code}.")

        if not os.path.exists(abs_folder):
            os.makedirs(abs_folder, exist_ok=True)

        custom_text = preserve_custom_content(abs_filepath)
        
        desc_clean = data['description'].replace('"', '')
        name_escaped = data['name'].replace('_', r'\_')
        desc_table = desc_clean.replace('|', r'\|')

        content = MD_TEMPLATE.format(
            error_code=code,
            desc_title=desc_clean,
            sqlstate=data['sqlstate'],
            error_name_escaped=name_escaped,
            description=desc_table,
            custom_content=custom_text
        )

        with open(abs_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if not file_exists:
            rel_path = f"reference/error-codes/{folder}/{filename}"
            title = f"Error {code}: {data['name']}"
            new_pages_for_summary.append((code, rel_path, title))

    if new_pages_for_summary:
        update_summary_file(new_pages_for_summary)
        print(f"[INFO] Generated {len(new_pages_for_summary)} brand new error pages.")
    else:
        print("[INFO] No new errors found. Documentation is fully up to date.")

if __name__ == "__main__":
    main()