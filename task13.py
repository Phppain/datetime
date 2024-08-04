"""task13.py"""

import os
import shutil

def move_contents(src_dirs, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for src_dir in src_dirs:
        if os.path.exists(src_dir):
            for item in os.listdir(src_dir):
                src_path = os.path.join(src_dir, item)
                dest_path = os.path.join(dest_dir, item)
                if os.path.isfile(src_path):
                    shutil.move(src_path, dest_path)
                elif os.path.isdir(src_path):
                    for file in os.listdir(src_path):
                        file_path = os.path.join(src_path, file)
                        shutil.move(file_path, dest_path)
        else:
            print(f"{src_dir} не найден")

if __name__ == "__main__":
    move_contents(['video', 'sub'], 'watch_me')
