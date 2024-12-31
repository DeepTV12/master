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
        # Ensure that each bot.js file is opened correctly in a new tmux pane
        command = f"tmux split-window -v 'cd {folder} && node bot.js'"
        subprocess.run(command, shell=True, check=True)
        time.sleep(1)
    except Exception as e:
        print(f"Error while running bot.js in {folder}: {e}")

def run_bots_in_tmux():
    # Create a new tmux session
    subprocess.run("tmux new-session -d -s bot_session", shell=True)
    time.sleep(1)

    # Start with the first bot.js
    subprocess.run(f"tmux send-keys 'cd {folders[0]} && node bot.js' C-m", shell=True)
    time.sleep(1)

    # Group bots into smaller batches to fit into tmux panes
    batch_size = 3  # Adjust this number based on the space you want to allocate per window
    for i in range(1, len(folders), batch_size):
        batch = folders[i:i+batch_size]

        # Create a new tmux window for each batch
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
