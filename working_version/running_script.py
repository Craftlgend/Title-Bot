import os
import sys

def check_script_running(script_name):
    lockfile_path = f"/tmp/{script_name}.lock"
    if os.path.isfile(lockfile_path):
        print(f"{script_name} is already running.")
        return True
    else:
        print(f"{script_name} is not running.")
        return False