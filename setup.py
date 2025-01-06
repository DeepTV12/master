import os
import sys

MASTER_DIR = os.path.dirname(os.path.abspath(__file__))  # Master repo directory

# Dictionary containing bot names and their respective token type (queryid/auth token)
BOT_TOKENS = {
    "Avacoin": "queryid",
    "AckiNack": "token",
    "SomeOtherBot": "queryid",  # Add other bots as needed
}

def update_datas_txt(bot_folder, key, value):
    """Appends a new entry to datas.txt inside a bot folder."""
    file_path = os.path.join(MASTER_DIR, bot_folder, 'datas.txt')

    # Ensure the bot folder exists
    if not os.path.exists(os.path.join(MASTER_DIR, bot_folder)):
        print(f"❌ Bot folder {bot_folder} not found! Skipping...")
        return

    # Read the existing content (if any)
    existing_content = ""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_content = f.read().strip()

    # Prepare new content
    new_entry = f"{key}: {value}\n"
    if existing_content:
        new_content = existing_content + "\n" + new_entry  # Append to existing content
    else:
        new_content = new_entry  # If empty, just add the new entry

    # Write the updated content back to the file
    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"✅ Updated {key} for {bot_folder} in {file_path}")

def main():
    for bot, token_type in BOT_TOKENS.items():
        print(f"🔍 Checking {bot}/datas.txt...")

        value = input(f"Enter {token_type} for {bot}: ").strip()

        update_datas_txt(bot, token_type, value)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Setup interrupted. Progress has been saved.")
        sys.exit(0)
