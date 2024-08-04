"""task9.py"""

def filter_file(input_file, bad_words_file, output_file):
    with open(bad_words_file, 'r') as f:
        bad_words = set(line.strip() for line in f)
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    with open(output_file, 'w') as f:
        for line in lines:
            words = line.split()
            filtered_line = ' '.join(word for word in words if word.lower() not in bad_words)
            f.write(filtered_line + '\n')

if __name__ == "__main__":
    filter_file('input.txt', 'bad_words.txt', 'output.txt')
