import os

# Check if Node.js is installed
def check_node():
    if os.system("node -v") != 0:
        print("🚀 Node.js is not installed. Installing Node.js and npm...")
        os.system("pkg update -y && pkg upgrade -y")
        os.system("pkg install nodejs -y")

# Install required npm packages
def install_npm_packages():
    print("📦 Installing required npm packages...")
    packages = "user-agents axios colors p-limit https-proxy-agent socks-proxy-agent crypto-js ws uuid xlsx cloudscraper readline-sync crypto pako"
    os.system(f"npm install -g {packages}")  # Global installation

# Run the functions
check_node()
install_npm_packages()

print("✅ All required packages have been installed successfully!")
