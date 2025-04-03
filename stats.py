def count_words(text):
    temp = text.split()
    return len(temp)

def sort_characters(characters):
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters

def count_characters(text):
    temp = text.lower()
    dict={}
    for char in temp:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
def report(file_path):
    text = get_book_text(file_path)
    characters = sort_characters(count_characters(text))
    words = count_words(text)
    print(print_separator('=', "BOOKBOT"))
    print(f"Analysing book found at: {file_path}")
    print(print_separator('-', "Word Count"))
    print(f"Found {words} total words")
    print(print_separator('-', "Character Count"))
    for k,v in characters:
        if k.isalpha():
            print(f"{k}: {v}")
    print(print_separator("=", "END"))

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def print_separator(character, text):
    counter = 33
    separator = ""
    for i in range(0,int((counter - (len(text)+2))/2)):
        separator += character

    output = separator + " " + text + " " + separator
    while len(output) < 33:
        output = character + output
    return output
