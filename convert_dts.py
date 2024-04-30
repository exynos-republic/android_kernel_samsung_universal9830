import sys
import re
import os

def convert_hex_to_int(match):
    hex_value = match.group(1)
    int_value = int(hex_value, 16)
    return str(int_value)

def convert_dts_file(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} is not a valid file.")
        return

    with open(input_file, 'r') as file:
        contents = file.read()

    # Regular expression to match hexadecimal values
    hex_pattern = r'(0x[0-9a-fA-F]+)'

    # Replace hexadecimal values with their integer equivalents
    converted_contents = re.sub(hex_pattern, convert_hex_to_int, contents)

    with open(input_file, 'w') as file:
        file.write(converted_contents)
        print(f"Converted: {input_file}")

# Usage: python script.py input_file1.dts input_file2.dts ...
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("n argument passed: " + str(len(sys.argv)))
        print("min argument allowed: 2")
        print("Usage: python script.py input_file1.dts input_file2.dts ...")
        sys.exit(1)

    input_files = sys.argv[1:]
    for input_file in input_files:
        convert_dts_file(input_file)