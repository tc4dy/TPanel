import os
import sys
import time
import ctypes

if sys.platform == 'win32':
    os.system('cls')

print("#" * 55)
print("      HIDDEN FILE & DIRECTORY DISCOVERY TOOL")
print("#" * 55)
print("\n")

search_path = input("[?] Enter Drive or Path to Scan (e.g., C:\\): ")

print(f"\n[*] Scanning {search_path} for hidden artifacts...")
print("[*] This may take a while depending on disk size...")
time.sleep(2)
print("-" * 55)

found_count = 0

try:
    for root, dirs, files in os.walk(search_path):
        for name in files:
            full_path = os.path.join(root, name)
            try:
                if sys.platform == 'win32':
                    attrs = ctypes.windll.kernel32.GetFileAttributesW(full_path)
                    if attrs != -1 and (attrs & 2):
                        print(f"[!] HIDDEN FOUND: {full_path}")
                        found_count += 1
                        time.sleep(0.05)
            except:
                continue
                
except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user.")

print("-" * 55)
print(f"[*] Scan finished. Total hidden files found: {found_count}")
input("Press Enter to exit...")