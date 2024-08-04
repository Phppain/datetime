"""task11.py"""

def merge_files():
    files = []
    while True:
        filename = input("Введите название файла (или 'quit' для завершения): ")
        if filename.lower() == 'quit':
            break
        files.append(filename)
    
    with open('merged_file.txt', 'w') as outfile:
        for filename in files:
            with open(filename, 'r') as infile:
                outfile.write(infile.read())

if __name__ == "__main__":
    merge_files()
