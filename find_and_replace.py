import os

# ==============================================================================
# --- CONFIGURATION ---
#
# Define the exact line to find and the line to replace it with.
# The script will match the entire line exactly.
#
LINE_TO_FIND = 'Rick James graciously allowed us to use this article in the Knowledge Base.'
REPLACEMENT_LINE = 'Rick James graciously allowed us to use this article in the documentation.'
#
# Define which file types to scan. Add more extensions as needed.
TARGET_EXTENSIONS = ('.md',)
#
# ==============================================================================


def process_file(file_path):
    """
    Reads a file, replaces the target line if found, and writes the changes back.

    Returns:
        bool: True if the file was modified, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
            lines = infile.readlines()
    except IOError as e:
        print(f"  [!] Could not read file {file_path}: {e}")
        return False

    was_modified = False
    new_lines = []

    for line in lines:
        # We strip trailing whitespace/newlines for a clean comparison
        if line.strip() == LINE_TO_FIND:
            # If it matches, append the replacement line, ensuring it has a newline
            new_lines.append(REPLACEMENT_LINE + '\n')
            was_modified = True
        else:
            # Otherwise, append the original line unchanged
            new_lines.append(line)

    if was_modified:
        try:
            with open(file_path, 'w', encoding='utf-8') as outfile:
                outfile.writelines(new_lines)
            print(f"  [+] Replaced line in: {os.path.basename(file_path)}")
        except IOError as e:
            print(f"  [!] Could not write to file {file_path}: {e}")
            return False

    return was_modified


def main():
    """Main function to drive the find-and-replace process."""
    print("--- Bulk Line Replacer ---")
    
    # --- SAFETY WARNING ---
    print("\n" + "="*60)
    print("!!! WARNING !!!")
    print("This script will permanently modify files in the target directory.")
    print("It is STRONGLY recommended to back up your files or use a")
    print("version control system (like git) before proceeding.")
    print("="*60 + "\n")

    # --- USER CONFIRMATION ---
    confirm = input("Are you sure you want to continue? (y/n): ")
    if confirm.lower() != 'y':
        print("Aborting script. No changes have been made.")
        return

    # --- GET DIRECTORY ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\nScript is located in: {script_dir}")
    repo_path_input = input("Press ENTER to scan this directory, or enter a different path: ")
    repo_path = repo_path_input.strip() or script_dir

    if not os.path.isdir(repo_path):
        print(f"[!] Error: The path '{repo_path}' is not a valid directory.")
        return

    modified_files = []
    file_count = 0
    print(f"\n[*] Starting scan in '{repo_path}'...")

    # --- SCAN AND PROCESS ---
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(TARGET_EXTENSIONS):
                file_count += 1
                full_path = os.path.join(root, file)
                if process_file(full_path):
                    modified_files.append(full_path)

    # --- FINAL REPORT ---
    print("\n--- Scan Complete ---")
    print(f"Searched {file_count} files with extensions: {TARGET_EXTENSIONS}")
    if modified_files:
        print(f"\nSuccessfully modified {len(modified_files)} file(s):")
        for f in modified_files:
            print(f" - {os.path.relpath(f, repo_path)}")
    else:
        print("\nNo files needed modification.")


if __name__ == '__main__':
    main()