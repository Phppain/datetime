"""task16.py"""

def remove_last_line(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    if len(lines) > 0:
        with open(output_file, 'w') as f:
            f.writelines(lines[:-1])

if __name__ == "__main__":
    remove_last_line('input.txt', 'output.txt')
