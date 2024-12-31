import os
import subprocess
from multiprocessing import Process

# List of folder names containing bot.js
folders = [
    "AckiNacki",
    "Agent301",
    "AngryMiner",
    "Animix",
    "AVACOIN",
    "AvaEthernity",
    "BettorWhale",
    "BirdsSui",
    "Bitminer",
    "Bits",
    "Bums",
    "BunnyBlizt",
    "BybitCoinsweeper",
    "BybitSpaceS",
    "CellWallet",
    "CoinRateCap",
    "Dormint",
    "DotCoin",
    "Fintopio",
    "FireCoin",
    "FlareX",
    "Gameness",
    "GenkiMiner",
    "Hamsterdam",
    "HamsterKombat",
    "HiPinPinAI",
    "IAMDOG",
    "Interstella",
    "KoniStory",
    "MoonHub",
    "NEUTON",
    "Nomis",
    "PandaScratch",
    "PellGEM",
    "PinEye",
    "Pixie",
    "PocketFI",
    "PocketRocket",
    "PocketWaifu",
    "RedPocket",
    "ReputationBuilder",
    "Roolz",
    "TonFREE",
    "TONxDAO",
    "UnitsWallet",
    "WhiteYescoin",
    "WonTon",
    "XPINPLANET",
    "XPointMaker",
    "YesCoin",
    "Zoo",
]

def run_bot(folder):
    try:
        # Navigate to the folder
        os.chdir(folder)
        print(f"Running bot.js in {folder}...")

        # Run bot.js with Node.js
        subprocess.run(["node", "bot.js"], check=True)
    except FileNotFoundError:
        print(f"Folder {folder} not found. Skipping...")
    except subprocess.CalledProcessError as e:
        print(f"Error while running bot.js in {folder}: {e}")
    finally:
        # Navigate back to the master folder
        os.chdir("..")

def run_bots_simultaneously():
    processes = []
    
    # Create a process for each bot to run in parallel
    for folder in folders:
        process = Process(target=run_bot, args=(folder,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

if __name__ == "__main__":
    run_bots_simultaneously()
