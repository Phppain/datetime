"""task12.py"""

def common_characters():
    files = []
    while True:
        filename = input("Введите название файла (или 'quit' для завершения): ")
        if filename.lower() == 'quit':
            break
        files.append(filename)
    
    common_chars = None
    for filename in files:
        with open(filename, 'r') as f:
            file_chars = set(f.read())
            if common_chars is None:
                common_chars = file_chars
            else:
                common_chars.intersection_update(file_chars)
    
    with open('common_chars.txt', 'w') as f:
        f.write(''.join(sorted(common_chars)))

if __name__ == "__main__":
    common_characters()
