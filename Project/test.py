import os
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(BASE_DIR, "test.txt")

with open(TEST_FILE, "r") as f:
    lines = f.read().splitlines()

for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        sort_type = lines[i]
        numbers = lines[i + 1]
        
        process = subprocess.Popen(
            ["python", "app.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            cwd=BASE_DIR,
            universal_newlines=True
        )
        
        try:
            print(f"[SEND] {sort_type}")
            process.stdin.write(sort_type + "\n")
            process.stdin.flush()
            time.sleep(0.1)

            print(f"[SEND] {numbers}")
            process.stdin.write(numbers + "\n")
            process.stdin.flush()
            time.sleep(0.1)

            output = process.stdout.readline().strip()
            print(f"[RECV] {output}")
            print("---")
        except Exception as e:
            print(f"[ERROR] {e}")
            print("---")
        finally:
            process.stdin.close()
            process.wait(timeout=2)

print("Test complete.")