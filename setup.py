import os

# Dictionary of bot names and their required type (queryid or token)
bots = {
    "Avacoin": "queryid",
    "AckiNack": "token",
    "Agent301": "queryid",
    "AngryMiner": "queryid",
    "Animix": "queryid",
    "AvaEthernity": "queryid",
    "BettorWhale": "queryid",
    "BirdsSui": "queryid",
    "BitMiner": "token",
    "Bits": "queryid",
    "Bums": "queryid",
    "BunnyBlizt": "queryid",
    "BybitCoinsweeper": "queryid",
    "BybitSpaceS": "queryid",
    "CellWallet": "queryid",
    "CoinRateCap": "token",
    "Dormint": "queryid",
    "Dotcoin": "queryid",
    "Fintopio": "queryid",
    "FireCoin": "queryid",
    "FlareX": "queryid",
    "GenkiMiner": "queryid",
    "Hamsterdam": "queryid",
    "HamsterKombat": "token",
    "HiPinPinAi": "queryid",
    "KoniStory": "queryid",
    "MoonHub": "queryid",
    "Neuton": "queryid",
    "Nomis": "queryid",
    "PandaScratch": "queryid",
    "PellGem": "queryid",
    "PocketFi": "queryid",
    "PocketRocket": "queryid",
    "RedPocket": "queryid",
    "Roolz": "queryid",
    "TONxDAO": "queryid",
    "TonFree": "queryid",
    "UnitsWallet": "token",
    "WhiteYescoin": "queryid",
    "WonTon": "queryid",
    "XPINPLANET": "queryid",
    "YesCoin": "queryid",
    "Zoo": "queryid",
}

# Function to update or append the correct value inside datas.txt
def update_datas_file(bot_name, bot_type, user_input):
    folder = bot_name  # Folder name is the bot name
    data_file = os.path.join(folder, "datas.txt")

    # If datas.txt does not exist, create it
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            f.write(f"{bot_type}: {user_input}\n")
        print(f"✅ Created {data_file} and saved {bot_type}.")
        return

    # Read current contents
    updated_lines = []
    found = False

    with open(data_file, "r") as f:
        lines = f.readlines()

    # Update existing value if found
    for line in lines:
        if line.startswith(f"{bot_type}:"):
            updated_lines.append(f"{bot_type}: {user_input}\n")
            found = True
        else:
            updated_lines.append(line)

    # If the entry was not found, append it
    if not found:
        updated_lines.append(f"{bot_type}: {user_input}\n")

    # Write updated content back to file
    with open(data_file, "w") as f:
        f.writelines(updated_lines)

    print(f"✅ Updated {bot_type} for {bot_name} in {data_file}")

# Main loop
if __name__ == "__main__":
    try:
        for bot, bot_type in bots.items():
            user_input = input(f"Please enter {bot_type} for {bot}: ").strip()

            if not user_input:
                print(f"⚠️ Skipping {bot} (empty input).")
                continue

            update_datas_file(bot, bot_type, user_input)

        print("\n✅ All bots have been configured successfully!")
    except KeyboardInterrupt:
        print("\n⏹️  Setup interrupted. Exiting safely... ✅")
