import os
import sys
import time

if sys.platform == 'win32':
    os.system('cls')

print("=" * 60)
print("          STORAGE ANALYSIS & DISK SPACE ENGINE")
print("=" * 60)
print("\n")

target_dir = input("[?] Enter directory to analyze (e.g., C:\\Users): ")
print(f"\n[*] Scanning directory: {target_dir}")
print("[*] Calculating file sizes... please wait.")
time.sleep(2)
print("-" * 60)

try:
    file_list = []
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                file_size = os.path.getsize(file_path)
                file_list.append((file_path, file_size))
            except:
                continue

    file_list.sort(key=lambda x: x[1], reverse=True)

    print(f"{'FILE PATH':<45} | {'SIZE (MB)':<10}")
    print("-" * 60)
    
    for path, size in file_list[:15]:
        size_mb = size / (1024 * 1024)
        print(f"{path[-42:]:>45} | {size_mb:>8.2f} MB")
        time.sleep(0.05)

except Exception as e:
    print(f"[-] Error: {e}")

print("-" * 60)
input("\nAnalysis complete. Press Enter to exit...")