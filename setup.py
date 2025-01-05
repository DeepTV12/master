import os
import sys

MASTER_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the master repo directory

def get_bot_folders():
    """Returns a list of bot folder names inside the master repository."""
    return [folder for folder in os.listdir(MASTER_DIR) if os.path.isdir(os.path.join(MASTER_DIR, folder))]

def update_datas_txt(bot_folder, key, value):
    """Updates datas.txt inside a specific bot folder."""
    file_path = os.path.join(MASTER_DIR, bot_folder, 'datas.txt')

    # Read existing lines if the file exists
    existing_lines = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_lines = f.readlines()

    # Update or add new entry
    updated_lines = []
    found = False
    for line in existing_lines:
        if line.startswith(f"{key}:"):
            updated_lines.append(f"{key}: {value}\n")
            found = True
        else:
            updated_lines.append(line)
    
    if not found:
        updated_lines.append(f"{key}: {value}\n")

    # Write back to datas.txt
    with open(file_path, 'w') as f:
        f.writelines(updated_lines)

    print(f"✅ Updated {key} for {bot_folder} in {file_path}")

def main():
    bot_folders = get_bot_folders()

    for bot in bot_folders:
        print(f"🔍 Checking {bot}/datas.txt...")

        key = input(f"Enter key for {bot} (e.g., queryid or token): ").strip()
        value = input(f"Enter value for {key} in {bot}: ").strip()

        update_datas_txt(bot, key, value)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Setup interrupted. Progress has been saved.")
        sys.exit(0)
