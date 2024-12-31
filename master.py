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

# Function to open each bot.js in a new tmux pane
def run_bot_in_tmux(folder):
    try:
        print(f"Opening tmux pane for {folder}...")
        # Run bot.js in a new tmux pane
        subprocess.run(f"tmux split-window -v 'cd {folder} && node bot.js'", shell=True)
        time.sleep(1)
    except Exception as e:
        print(f"Error while running bot.js in {folder}: {e}")

def run_bots_in_tmux():
    # Create a new tmux session with a fixed window size (e.g., 80 columns, 24 rows)
    subprocess.run("tmux new-session -d -s bot_session", shell=True)
    time.sleep(1)

    # Set up the first pane with the first bot.js
    subprocess.run(f"tmux send-keys 'cd {folders[0]} && node bot.js' C-m", shell=True)
    time.sleep(1)

    # Start splitting the window for the other bots
    for folder in folders[1:]:
        run_bot_in_tmux(folder)
    
    # Adjust the layout to evenly distribute space across all the panes
    subprocess.run("tmux select-layout even-vertical", shell=True)
    
    # Attach to the tmux session to see the output
    subprocess.run("tmux attach-session -t bot_session", shell=True)

if __name__ == "__main__":
    run_bots_in_tmux()
