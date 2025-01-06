import os
import sys

# Set the master repository directory
MASTER_DIR = os.path.dirname(os.path.abspath(__file__))

# Define bot folders and their respective token types
BOTS = {
    "AVACOIN": "queryid",
    "AckiNacki": "token",
    "Agent301": "queryid",
    "AngryMiner": "queryid",
    "Animix": "queryid",
    "AvaEthernity": "queryid",
    "BettorWhale": "queryid",
    "BirdsSui": "queryid",
    "Bitminer": "token",
    "Bits": "queryid",
    "Bums": "queryid",
    "BunnyBlizt": "queryid",
    "BybitCoinsweeper": "queryid",
    "BybitSpaceS": "queryid",
    "CellWallet": "queryid",
    "CoinRateCap": "token",
    "Dormint": "queryid",
    "DotCoin": "queryid",
    "Fintopio": "queryid",
    "FireCoin": "queryid",
    "FlareX": "queryid",
    "Gameness": "queryid",
    "GenkiMiner": "queryid",
    "HamsterKombat": "token",
    "Hamsterdam": "queryid",
    "HiPinPinAI": "queryid",
    "Interstella": "queryid",
    "KoniStory": "queryid",
    "MoonHub": "queryid",
    "NEUTON": "queryid",
    "Nomis": "queryid",
    "PandaScratch": "queryid",
    "PellGEM": "queryid",
    "PinEye": "queryid",
    "Pixie": "queryid",
    "PocketFI": "queryid",
    "PocketRocket": "queryid",
    "RedPocket": "queryid",
    "Roolz": "queryid",
    "TonFREE": "queryid",
    "TONxDAO": "queryid",
    "UnitsWallet": "token",
    "WhiteYescoin": "queryid",
    "WonTon": "queryid",
    "XPINPLANET": "queryid",
    "YesCoin": "queryid",
    "Zoo": "queryid"
}

def update_datas_txt(bot_folder, value):
    """Updates the datas.txt file in the bot folder."""
    file_path = os.path.join(MASTER_DIR, bot_folder, 'datas.txt')

    # Check if bot folder exists
    if not os.path.exists(os.path.join(MASTER_DIR, bot_folder)):
        print(f"❌ Folder '{bot_folder}' not found! Skipping...")
        return

    # Read existing content
    existing_content = ""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_content = f.read().strip()

    # Prepare new content
    new_entry = f"{value}\n"
    if existing_content:
        new_content = existing_content + "\n" + new_entry  # Append if content exists
    else:
        new_content = new_entry  # Just add the new entry if file is empty

    # Write the updated content back
    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"✅ Updated {bot_folder}")

def main():
    for bot_folder in BOTS.keys():
        print(f"🔍 Checking {bot_folder}/datas.txt...")

        value = input(f"Enter value for {bot_folder}: ").strip()

        update_datas_txt(bot_folder, value)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Setup interrupted. Progress has been saved.")
        sys.exit(0)
