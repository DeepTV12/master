import os
import subprocess

# Define the path to your main folder
main_folder_path = './master'  # Adjust based on your cloned GitHub repository structure

# Function to run the JS file (bot.js or 1.js) in a folder
def run_js_file(folder_path):
    try:
        # Navigate into the folder
        os.chdir(folder_path)

        # Check if bot.js or 1.js exists in the folder
        if os.path.exists('bot.js'):
            js_file = 'bot.js'
        elif os.path.exists('1.js'):
            js_file = '1.js'
        else:
            print(f"No bot.js or 1.js found in {folder_path}. Skipping...")
            return

        # Run the command as it would be in Termux
        print(f"Running {js_file} in {folder_path}...")
        command = f"node {js_file}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Capture output and errors
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(f"Success: {folder_path}/{js_file} - {stdout.decode()}")
        else:
            print(f"Error in {folder_path}/{js_file} - {stderr.decode()}")

    except Exception as e:
        print(f"Failed to execute script in {folder_path}: {str(e)}")

    finally:
        # Navigate back to the main folder
        os.chdir('..')

# Main function to execute the scripts in all subfolders
def run_all_js_files():
    # Step 1: Get all subfolders in the main folder
    if not os.path.exists(main_folder_path):
        print(f"Main folder path does not exist: {main_folder_path}")
        return

    subfolders = [os.path.join(main_folder_path, folder) for folder in os.listdir(main_folder_path) if os.path.isdir(os.path.join(main_folder_path, folder))]

    if not subfolders:
        print("No subfolders found in the main folder.")
        return

    # Step 2: Run either bot.js or 1.js in each subfolder
    for subfolder in subfolders:
        print(f"Processing folder: {subfolder}")
        run_js_file(subfolder)

if __name__ == '__main__':
    run_all_js_files()
