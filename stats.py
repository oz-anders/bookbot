def get_num_words(text):  # Fixed the missing colon
    words = text.split()  # Use split() to break text into words
    return len(words)     # Return the count of words
def get_char_count(text):
    char_count = {}
    lower_case_book = text.lower()
    for letter in lower_case_book:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count
def sort_on(dict):
    return dict["num"]
def sort_characters(characters):
    sorted_char = [] # empty list for dictionaries.
    for char, count in characters.items():
        if char.isalpha():
            char_dict = {"char": char,"num": count}
            sorted_char.append(char_dict)
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char