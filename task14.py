"""task14.py"""

import os

def rename_files():
    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            parts = filename.replace('.jpg', '').split('_')
            if len(parts) == 2:
                new_name = f"{parts[1]}_{parts[0]}.jpg"
                os.rename(filename, new_name)

if __name__ == "__main__":
    rename_files()
