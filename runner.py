import os
import subprocess

for file in os.listdir():
    if file.endswith(".py") and file != "runner.py":
        print(f"تشغيل {file} الآن...")
        subprocess.Popen(["python3", file])