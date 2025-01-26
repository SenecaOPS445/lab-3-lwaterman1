#!/usr/bin/env python3
#Author ID: 123151235

import subprocess

def free_space():

    try:
    
        result = subprocess.run(
            "df -h | grep '/$' | awk '{print $4}'",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
    )
        if result.returncode == 0:
        
            return result.stdout.strip()
        else:
        
            raise RuntimeError(f"Error executing command: {result.stderr.strip()}")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":

    print(free_space())
