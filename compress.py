import re

def compress_code(input_string):
    main_dict = {}
    current_key = 1

    words = re.findall(r'\b(?!\d+\b)\w{1,}\b', input_string)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        if count >= 2 and len(word) >= 6:
            if word not in main_dict.values():
                main_dict[current_key] = word
                current_key += 1

    compressed_string = input_string
    output = ""
    for key, value in main_dict.items():
        compressed_string = re.sub(rf'\b{re.escape(value)}\b', rf'\\{key}\\', compressed_string)
        output += f"{key}:{value},"

    return output.strip() + "\n" + compressed_string.strip()