import os
import subprocess
from multiprocessing import Pool

# Define the path to your main folder, assuming the script is cloned into the 'master' folder
main_folder_path = './master'  # Adjust this path if needed

# Function to run each bot.js file
def run_bot_script(bot_path):
    try:
        # Run the bot.js file using Node.js
        process = subprocess.Popen(['node', bot_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Capture the output and error (if any)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            print(f'Success: {bot_path} - {stdout.decode()}')
        else:
            print(f'Error in {bot_path} - {stderr.decode()}')
    
    except Exception as e:
        print(f'Failed to execute {bot_path}: {str(e)}')

# Function to get all the bot.js files
def get_bot_paths(main_folder):
    bot_paths = []
    
    # Walk through the folder and find bot.js files in the subfolders
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file == 'bot.js':
                bot_paths.append(os.path.join(root, file))
    
    return bot_paths

# Main function to execute the bots concurrently
def run_all_bots():
    # Step 1: Get all bot.js file paths
    bot_paths = get_bot_paths(main_folder_path)
    
    if not bot_paths:
        print("No bot.js files found.")
        return
    
    # Step 2: Run all the bot.js files concurrently using multiprocessing
    with Pool(processes=len(bot_paths)) as pool:
        pool.map(run_bot_script, bot_paths)

if __name__ == '__main__':
    run_all_bots()
