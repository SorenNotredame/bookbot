from stats import count_words, count_characters, sorted_characters
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")


    for dict in sorted_characters(count_characters(text)):
        print(f"{dict['char']}: {dict['num']}")

main()