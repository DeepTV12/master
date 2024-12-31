import os
import subprocess
import time

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

# Function to open each bot.js in a separate tmux pane
def run_bot_in_tmux(folder):
    try:
        print(f"Opening tmux window for {folder}...")
        
        # Start a new tmux session and create a new window for each bot
        subprocess.run(f"tmux new-session -d -s bot_session 'cd {folder} && node bot.js'", shell=True)
        
        # Wait to ensure tmux has enough time to set up
        time.sleep(1)
        
    except FileNotFoundError:
        print(f"Folder {folder} not found. Skipping...")
    except Exception as e:
        print(f"Error while running bot.js in {folder}: {e}")

def run_bots_in_tmux():
    # Create a new tmux session
    subprocess.run("tmux new-session -d -s bot_session", shell=True)
    
    # Iterate through each folder and open each bot in a separate tmux pane
    for folder in folders:
        run_bot_in_tmux(folder)
    
    # Attach to the tmux session to see all the panes running
    subprocess.run("tmux attach-session -t bot_session", shell=True)

if __name__ == "__main__":
    run_bots_in_tmux()
