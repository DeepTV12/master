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

# Function to prompt the user for input and save to datas.txt
def setup_bot(bot_name, bot_type):
    folder = bot_name  # Assuming folder names match bot names exactly
    data_file = os.path.join(folder, "datas.txt")

    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Ask the user for the required input (queryid or token)
    user_input = input(f"Please enter {bot_type} for {bot_name}: ")

    # Use Termux-compatible command to append input to datas.txt
    command = f'echo "{bot_type}: {user_input}" >> "{data_file}"'
    os.system(command)

    print(f"Saved {bot_type} for {bot_name} in {data_file} ✅")

# Main loop
if __name__ == "__main__":
    for bot, bot_type in bots.items():
        setup_bot(bot, bot_type)

    print("\n✅ All bots have been configured successfully!")
