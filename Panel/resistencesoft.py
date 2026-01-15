import os
import sys
import shutil
import time

if sys.platform == 'win32':
    os.system('cls')

print("B" * 60)
print("        SYSTEM PERSISTENCE MECHANISM SIMULATOR")
print("B" * 60)

print("\n[*] Analyzing system startup configuration...")
time.sleep(1.5)

try:
    script_path = os.path.realpath(sys.argv[0])
    appdata = os.getenv('APPDATA')
    startup_path = os.path.join(appdata, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    target_file = os.path.join(startup_path, "system_service.py")

    print(f"[*] Target location: {startup_path}")
    print("[*] Deploying persistence module...")
    time.sleep(2)

    if not os.path.exists(target_file):
        shutil.copy(script_path, target_file)
        print("\n" + "=" * 40)
        print("[+] SUCCESS: Script added to Startup.")
        print("[+] This tool will run every time the PC boots.")
        print("=" * 40)
    else:
        print("\n[!] Module already exists in target location.")
        choice = input("\n[?] Do you want to remove it? (y/n): ")
        if choice.lower() == 'y':
            os.remove(target_file)
            print("[+] Persistence removed.")

except Exception as e:
    print(f"\n[-] Critical Error: Ensure you have write permissions. {e}")

input("\nOperation complete. Press Enter to exit...")