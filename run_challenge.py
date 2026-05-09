# run_challenge.py
# Simple countdown timer utility

import time
import sys

def countdown(seconds: int):
    print(f"Starting countdown from {seconds}...")
    for i in range(seconds, 0, -1):
        print(f"  {i}...", end="\r")
        time.sleep(1)
    print("  Done!       ")

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    countdown(n)
