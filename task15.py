"""task15.py"""

import os
import shutil

def move_files_from_list(list_file, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(list_file, 'r') as f:
        files = f.readlines()
    
    for file_name in files:
        file_name = file_name.strip()
        if os.path.isfile(file_name):
            shutil.move(file_name, os.path.join(dest_dir, file_name))
        else:
            print(f"Файл {file_name} не найден")

if __name__ == "__main__":
    move_files_from_list('list.tsv', 'list')
