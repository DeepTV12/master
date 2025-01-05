import os
import subprocess
from multiprocessing import Pool, cpu_count

# List of folder names containing bot.js or 1.js
folders = [
    "AckiNacki", "Agent301", "AngryMiner", "Animix", "AVACOIN", "AvaEthernity", "BettorWhale", "BirdsSui", "Bitminer", "Bits", "Bums", "BunnyBlizt", 
    "BybitCoinsweeper", "BybitSpaceS", "CellWallet", "CoinRateCap", "Dormint", "DotCoin", "Fintopio", "FireCoin", "FlareX", "Gameness", "GenkiMiner", 
    "Hamsterdam", "HamsterKombat", "HiPinPinAI", "Interstella", "KoniStory", "MoonHub", "NEUTON", "Nomis", "PandaScratch", "PellGEM", 
    "PinEye", "Pixie", "PocketFI", "PocketRocket", "RedPocket", "Roolz", "TonFREE", "TONxDAO", "UnitsWallet", 
    "WhiteYescoin", "WonTon", "XPINPLANET", "YesCoin", "Zoo"
]

# Function to run a bot.js or 1.js script in a folder
def run_bot(folder):
    try:
        print(f"Running bot in {folder}...")
        os.chdir(folder)  # Change to the folder
        if os.path.exists("bot.js"):
            subprocess.run("node bot.js", shell=True, check=True)
        elif os.path.exists("1.js"):
            subprocess.run("node 1.js", shell=True, check=True)
        else:
            print(f"No bot.js or 1.js found in {folder}")
        os.chdir("..")  # Change back to the parent directory
    except Exception as e:
        print(f"Error in {folder}: {e}")

def main():
    # Get the number of CPUs available
    num_workers = min(len(folders), cpu_count())  # Use the number of folders or CPUs, whichever is smaller

    # Create a process pool
    with Pool(processes=num_workers) as pool:
        pool.map(run_bot, folders)  # Run the function on all folders in parallel

if __name__ == "__main__":
    main()
