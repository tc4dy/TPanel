import os
import time
import sys

if sys.platform == 'win32':
    os.system('cls')

print("!" * 60)
print("       FILE EXTENSION MASQUERADER & SECURITY TOOL")
print("!" * 60)
print("\n")

folder_path = input("[?] Enter directory path to process: ")
print("\n[1] Lock Files (Change to .locked)")
print("[2] Unlock Files (Restore to .txt)")
choice = input("\n[?] Select Operation Mode (1/2): ")

if choice == '1':
    old_ext = ".txt"
    new_ext = ".locked"
    action = "Locking"
elif choice == '2':
    old_ext = ".locked"
    new_ext = ".txt"
    action = "Unlocking"
else:
    print("[-] Invalid selection.")
    sys.exit()

print(f"\n[*] {action} files in target directory...")
time.sleep(1)

try:
    count = 0
    files = os.listdir(folder_path)
    for filename in files:
        if filename.endswith(old_ext):
            base = os.path.splitext(filename)[0]
            new_name = base + new_ext
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
            print(f"[+] Processed: {filename} -> {new_name}")
            count += 1
            time.sleep(0.1)
    
    if count == 0:
        print("[-] No matching files found.")
    else:
        print(f"\n[*] Success! {count} files processed.")

except FileNotFoundError:
    print("[-] Error: Directory not found.")
except Exception as e:
    print(f"[-] Critical Error: {e}")

input("\nPress Enter to exit...")