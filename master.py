import os
import subprocess
import time

def run_bot(folder):
    try:
        print(f"Running bot in {folder} for 3 minutes...")
        os.chdir(folder)  # Change to the folder
        process = None
        
        if os.path.exists("bot.js"):
            process = subprocess.Popen("node bot.js", shell=True)
        elif os.path.exists("1.js"):
            process = subprocess.Popen("node 1.js", shell=True)
        else:
            print(f"No bot.js or 1.js found in {folder}")
        
        time.sleep(100)  # Wait for 100 seconds
        
        if process:
            process.terminate()  # Terminate the process after 3 minutes
            print(f"Stopped bot in {folder}")
        
        os.chdir("..")  # Change back to the parent directory
    except Exception as e:
        print(f"Error in {folder}: {e}")

def main():
    while True:
        for folder in folders:
            run_bot(folder)
            print("Waiting 3 minutes before starting the next bot...")
            time.sleep(3)  # Wait for 3 seconds before starting the next bot

if __name__ == "__main__":
    folders = [
        "AckiNacki", "Agent301", "AngryMiner", "Animix", "AVACOIN", "AvaEthernity", "BettorWhale", "BirdsSui", "Bitminer", "Bits", "Bums", "BunnyBlizt", 
        "BybitCoinsweeper", "BybitSpaceS", "CellWallet", "CoinRateCap", "Dormint", "DotCoin", "Fintopio", "FireCoin", "FlareX", "Gameness", "GenkiMiner", 
        "Hamsterdam", "HamsterKombat", "HiPinPinAI", "Interstella", "KoniStory", "MoonHub", "NEUTON", "Nomis", "PandaScratch", "PellGEM", 
        "PinEye", "Pixie", "PocketFI", "PocketRocket", "RedPocket", "Roolz", "TonFREE", "TONxDAO", "UnitsWallet", 
        "WhiteYescoin", "WonTon", "XPINPLANET", "YesCoin", "Zoo"
    ]
    
    main()
