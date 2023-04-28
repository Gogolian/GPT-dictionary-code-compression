import sys
import os
from compress import compress_code
from remove_python_comments import remove_python_comments

def main():
    if len(sys.argv) < 2:
        print("Usage: python compress_file.py <filename>")
        return

    input_filename = sys.argv[1]
    if not os.path.isfile(input_filename):
        print(f"Error: {input_filename} is not a valid file.")
        return

    # Read the input file
    with open(input_filename, 'r') as input_file:
        input_code = input_file.read()


    # remove python comments:
    input_code = remove_python_comments(input_code)


    # Compress the input code
    compressed_code = compress_code(input_code)

    # Save the compressed code to a new file
    output_filename = os.path.splitext(input_filename)[0] + "-compressed" + os.path.splitext(input_filename)[1]
    with open(output_filename, 'w') as output_file:
        # Write the compressed code to the file
        output_file.write(compressed_code)

    print(f"Compressed code saved to {output_filename}")

if __name__ == "__main__":
    main()
