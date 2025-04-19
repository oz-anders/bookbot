import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words

from stats import get_char_count

from stats import sort_characters

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    count = get_num_words(text)  # Call the function with text as parameter
    characters = get_char_count(text)
    sort = sort_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words" )
    print("--------- Character Count -------")
    for item in sort:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()