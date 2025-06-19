import os
import re

def fix_markdown_links_in_repo(repo_path):
    """
    Scans a directory recursively for Markdown (.md) files and removes
    backticks that enclose a complete markdown link.

    Example: '`[text](link)`' becomes '[text](link)'
    """
    # This regular expression is key. It looks for:
    # `          - A literal backtick
    # (          - Start a capturing group (this is what we want to keep)
    # \[.*?\]    - A literal '[', any characters (non-greedy), then a literal ']'
    # \(.*?\)    - A literal '(', any characters (non-greedy), then a literal ')'
    # )          - End the capturing group
    # `          - A literal backtick
    link_pattern = re.compile(r'`(\[.*?\]\(.*?\))`')

    print(f"[*] Starting scan in directory: {repo_path}\n")
    files_changed = 0

    # os.walk is perfect for traversing a directory tree
    for root_dir, _, filenames in os.walk(repo_path):
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(root_dir, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Check if the problematic pattern exists before modifying
                    if link_pattern.search(content):
                        # The .sub() method replaces the entire match with just
                        # the part inside the capturing group (r'\1').
                        new_content = link_pattern.sub(r'\1', content)

                        # Only write back to the file if changes were made
                        if new_content != content:
                            print(f"[*] Fixing links in: {file_path}")
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            files_changed += 1

                except Exception as e:
                    print(f"[!] Error processing file {file_path}: {e}")

    print(f"\n[*] Scan complete. Total files changed: {files_changed}")

if __name__ == "__main__":
    # Get the current working directory, which should be the root of your repo
    current_directory = os.getcwd()
    fix_markdown_links_in_repo(current_directory)