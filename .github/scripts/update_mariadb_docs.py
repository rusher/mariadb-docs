import os
import re
import urllib.request

# --- Configuration ---
# In GitHub Actions, the script runs from the root of the repository
DOCS_ROOT = '.' 
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
            print(f"[INFO] Download complete. Found {len(lines)} lines of text.")
    except Exception as e:
        print(f"[ERROR] Failed to fetch the file: {e}")
        return {}

    print("[INFO] Parsing error codes...")
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
    """Calculates the 100-batch folder name for a given error code."""
    start = (code // 100) * 100
    end = start + 99
    return f"mariadb-error-codes-{start}-to-{end}"

def preserve_custom_content(file_path):
    """Extracts custom user text to prevent overwriting."""
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
    """Appends new error pages to SUMMARY.md."""
    if not os.path.exists(SUMMARY_FILE):
        print(f"[WARNING] {SUMMARY_FILE} not found. Skipping GitBook summary update.")
        return

    print(f"[INFO] Updating GitBook SUMMARY.md with {len(new_pages)} new entries...")
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
                to_add = pages_by_range[range_start]
                for code, path, title in to_add:
                    path_check = f"/{os.path.basename(path)}"
                    already_exists = any(path_check in l for l in lines)
                    if not already_exists:
                        indent = "    " if line.startswith("  *") else "  "
                        entry = f"{indent}* [{title}]({path})\n"
                        new_lines.append(entry)

    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    print("=" * 70)
    print(" DOCS-5990: MariaDB Error Code Automation (GitHub Actions) ")
    print("=" * 70)
    
    errors = parse_errmsg_file(ERRMSG_URL)
    if not errors:
        print("[ERROR] No errors parsed. Exiting script.")
        return
    
    print(f"[INFO] Successfully fetched and parsed {len(errors)} error codes.")
    
    new_pages_for_summary = []

    for code, data in errors.items():
        folder = get_folder_name(code)
        filename = f"e{code}.md"
        
        abs_folder = os.path.join(ERROR_CODES_DIR, folder)
        abs_filepath = os.path.join(abs_folder, filename)
        
        is_unused = data['name'].startswith("ER_UNUSED_")
        file_exists = os.path.exists(abs_filepath)

        # Skip logic
        if is_unused and not file_exists:
            continue
        elif is_unused and file_exists:
            print(f"[ACTION] OVERWRITE: Error {code} downgraded to unused.")
        elif file_exists:
            continue
        else:
            print(f"[ACTION] CREATE: Missing documentation for Error {code} ({data['name']}).")

        # Ensure directory exists
        if not os.path.exists(abs_folder):
            os.makedirs(abs_folder, exist_ok=True)

        # Content preservation
        custom_text = preserve_custom_content(abs_filepath)
        
        # Format Data
        desc_clean = data['description'].replace('"', '')
        name_escaped = data['name'].replace('_', r'\_')
        desc_table = desc_clean.replace('|', r'\|')

        # Compile Markdown
        content = MD_TEMPLATE.format(
            error_code=code,
            desc_title=desc_clean,
            sqlstate=data['sqlstate'],
            error_name_escaped=name_escaped,
            description=desc_table,
            custom_content=custom_text
        )

        # Write to disk
        with open(abs_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Track new files for SUMMARY.md
        if not file_exists:
            rel_path = f"reference/error-codes/{folder}/{filename}"
            title = f"Error {code}: {data['name']}"
            new_pages_for_summary.append((code, rel_path, title))

    if new_pages_for_summary:
        update_summary_file(new_pages_for_summary)
        print(f"[INFO] Generated {len(new_pages_for_summary)} brand new error pages.")
    else:
        print("[INFO] No new errors found. Documentation is fully up to date.")

    print("=" * 70)
    print(" Automation Complete. ")
    print("=" * 70)

if __name__ == "__main__":
    main()