import os
import subprocess
import time

# List of folder names containing bot.js
folders = [
    "AckiNacki", "Agent301", "AngryMiner", "Animix", "AVACOIN", "AvaEthernity", "BettorWhale", "BirdsSui", "Bitminer", "Bits", "Bums", "BunnyBlizt", 
    "BybitCoinsweeper", "BybitSpaceS", "CellWallet", "CoinRateCap", "Dormint", "DotCoin", "Fintopio", "FireCoin", "FlareX", "Gameness", "GenkiMiner", 
    "Hamsterdam", "HamsterKombat", "HiPinPinAI", "IAMDOG", "Interstella", "KoniStory", "MoonHub", "NEUTON", "Nomis", "PandaScratch", "PellGEM", 
    "PinEye", "Pixie", "PocketFI", "PocketRocket", "PocketWaifu", "RedPocket", "ReputationBuilder", "Roolz", "TonFREE", "TONxDAO", "UnitsWallet", 
    "WhiteYescoin", "WonTon", "XPINPLANET", "XPointMaker", "YesCoin", "Zoo"
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

    # Start with the first bot.js
    subprocess.run(f"tmux send-keys 'cd {folders[0]} && node bot.js' C-m", shell=True)
    time.sleep(1)

    # Grouping bots into manageable chunks (e.g., 5 bots per window)
    batch_size = 5
    for i in range(1, len(folders), batch_size):
        batch = folders[i:i+batch_size]

        # For each batch, create a new tmux window
        subprocess.run("tmux new-window", shell=True)
        time.sleep(1)

        # Open each bot.js in the new window
        for folder in batch:
            run_bot_in_tmux(folder)
        
        # Adjust the layout of the tmux window (vertical split for each bot)
        subprocess.run("tmux select-layout even-vertical", shell=True)
    
    # Finally, attach to the tmux session to see the running processes
    subprocess.run("tmux attach-session -t bot_session", shell=True)

if __name__ == "__main__":
    run_bots_in_tmux()
