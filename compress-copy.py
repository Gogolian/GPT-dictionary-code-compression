import sys
from tqdm import tqdm

def compress_code(code, max_length=10):
    # Initialize an empty dictionary to store the mappings
    dictionary = {}

    # Find all repeated substrings of length 3 or more and up to max_length in the code
    substrings = set()
    for i in range(3, min(len(code) + 1, max_length + 1)):
        for j in range(len(code) - i + 1):
            substring = code[j:j + i]
            if substring in substrings:
                # Add the repeated substring to the dictionary with a new code
                if substring not in dictionary:
                    code = code.replace(substring, str(len(dictionary) + 1))
                    dictionary[str(len(dictionary) + 1)] = substring
            else:
                substrings.add(substring)

        # Update the progress bar after each iteration
        progress = (i / min(len(code), max_length)) * 100
        tqdm.write(f"Progress: {progress:.2f}%")

    # Generate the compressed code using the dictionary and template
    compressed_code = ""
    for line in code.split("\n"):
        if line.strip() == "":
            # Ignore empty lines
            continue
        # Substitute each word in the line with its code if it is in the dictionary
        compressed_line = ""
        for word in line.split():
            if word in dictionary:
                compressed_line += dictionary[word] + " "
            else:
                compressed_line += word + " "
        # Remove the trailing space and add the compressed line to the result
        compressed_code += compressed_line.strip() + "\n"

    # Generate the output string using the dictionary
    output = ""
    for code_num, substring in dictionary.items():
        # Check if the substring contains only letters and spaces
        if all(c.isalpha() or c.isspace() for c in substring):
            # Add the substring to the output with its code number
            output += f"{code_num}: {substring}\n"

    # Replace the remaining code numbers in the compressed code with the corresponding substring
    for code_num, substring in dictionary.items():
        compressed_code = compressed_code.replace(code_num, substring)


    # Return the final output and compressed code
    return output.strip() + "\n" + compressed_code.strip()