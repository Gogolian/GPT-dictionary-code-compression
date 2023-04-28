import re

def remove_python_comments(input_string):
    # Remove single-line comments
    input_string = re.sub(r'#.*$', '', input_string, flags=re.MULTILINE)

    # Remove multi-line comments
    input_string = re.sub(r'\'\'\'.*?\'\'\'', '', input_string, flags=re.DOTALL)
    input_string = re.sub(r'""".*?"""', '', input_string, flags=re.DOTALL)

    return input_string