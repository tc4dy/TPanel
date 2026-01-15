import time
import os
import sys

if sys.platform == 'win32':
    os.system('cls')

print("~" * 50)
print("          TEXT ANALYTICS & METRICS SUITE")
print("~" * 50)
print("\n")

text_input = input("[?] Enter or Paste Text to Analyze: \n> ")

print("\n[*] Processing natural language data...")
time.sleep(1.2)

char_count = len(text_input)
word_count = len(text_input.split())
line_count = len(text_input.splitlines())
space_count = text_input.count(' ')

print("\n" + "-" * 30)
print(f"Total Characters : {char_count}")
print(f"Total Words      : {word_count}")
print(f"Total Lines      : {line_count}")
print(f"Total Spaces     : {space_count}")
print("-" * 30)

input("\nMetrics calculated. Press Enter to exit...")