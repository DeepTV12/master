import subprocess
import os

# List of paths to bot.js files
bot_js_paths = [
    "C:\\Users\\cf\\Desktop\\Airdrops\\AckiNacki\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Agent301\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\AngryMiner\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Animix\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\AVACOIN\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\AvaEthernity\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\BettorWhale\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\BirdsSui\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Bitminer\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Bits\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Bums\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\BunnyBlizt\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\BybitCoinsweeper\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\BybitSpaceS\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\CellWallet\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\CoinRateCap\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Dormint\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\DotCoin\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Fintopio\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\FireCoin\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\FlareX\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Gameness\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\GenkiMiner\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Hamsterdam\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\HamsterKombat\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\HiPinPinAI\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\IAMDOG\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Interstella\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\KoniStory\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\MoonHub\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\NEUTON\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Nomis\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\PandaScratch\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\PellGEM\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\PinEye\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Pixie\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\PocketFI\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\PocketRocket\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\PocketWaifu\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\RedPocket\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\ReputationBuilder\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Roolz\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\TonFREE\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\TONxDAO\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\UnitsWallet\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\WhiteYescoin\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\WonTon\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\XPINPLANET\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\XPointMaker\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\YesCoin\\bot.js",
    "C:\\Users\\cf\\Desktop\\Airdrops\\Zoo\\bot.js",
]

def run_bots():
    processes = []

    for bot_path in bot_js_paths:
        if not os.path.exists(bot_path):
            print(f"File not found: {bot_path}. Skipping...")
            continue

        # Get the folder path
        folder_path = os.path.dirname(bot_path)
        print(f"Processing folder: {folder_path}")

        try:
            # Run the bot.js file using `node`
            process = subprocess.Popen(
                ['node', bot_path],
                cwd=folder_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            processes.append((process, folder_path))
            print(f"Running bot.js in {folder_path}...")
        except Exception as e:
            print(f"Failed to run bot.js in {folder_path}: {e}")

    # Monitor all processes
    for process, folder in processes:
        try:
            stdout, stderr = process.communicate(timeout=60)
            print(f"Output from {folder}:\n{stdout}")
            if stderr:
                print(f"Errors from {folder}:\n{stderr}")
        except subprocess.TimeoutExpired:
            print(f"Timeout: {folder}/bot.js took too long to execute and was terminated.")
            process.kill()

if __name__ == '__main__':
    run_bots()
