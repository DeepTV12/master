import os
import subprocess
from multiprocessing import Pool

# Define the path to your main folder (assumes it's cloned to 'master')
main_folder_path = './master'  # Adjust the path if needed

# Function to run the JavaScript file
def run_js_file(js_file_path):
    try:
        # Run the JavaScript file using Node.js
        process = subprocess.Popen(['node', js_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Capture the output and error (if any)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            print(f'Success: {js_file_path} - {stdout.decode()}')
        else:
            print(f'Error in {js_file_path} - {stderr.decode()}')
    
    except Exception as e:
        print(f'Failed to execute {js_file_path}: {str(e)}')

# Function to find either bot.js or 1.js files
def get_js_file_paths(main_folder):
    js_file_paths = []
    
    # Walk through the folder and find bot.js or 1.js files in the subfolders
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file == 'bot.js' or file == '1.js':  # Check for both bot.js and 1.js
                js_file_paths.append(os.path.join(root, file))
    
    return js_file_paths

# Main function to execute the scripts concurrently
def run_all_js_files():
    # Step 1: Get all bot.js or 1.js file paths
    js_file_paths = get_js_file_paths(main_folder_path)
    
    if not js_file_paths:
        print("No bot.js or 1.js files found.")
        return
    
    # Step 2: Run all the JavaScript files concurrently using multiprocessing
    with Pool(processes=len(js_file_paths)) as pool:
        pool.map(run_js_file, js_file_paths)

if __name__ == '__main__':
    run_all_js_files()
