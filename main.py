from stats import count_words, sort_dicts
from stats import count_character
import sys

def get_book_text(file_path):
    print(f"Analyzing book found at {file_path}")
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return

    print("============ BOOKBOT ============")
    text = get_book_text(sys.argv[1])
    numb_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {numb_words} total words")

    print("----------- Character Count ----------")
    characters_count = count_character(text)
    sorted_dicts = sort_dicts(characters_count)
    for dict in sorted_dicts:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
main()
