from stats import (
words_in_book,
total_characters_used,
book_report)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1] # path to txt file
    book_text = get_book_text(book_path) # turns file into a string
    num_words = words_in_book(book_text) # returns total number of words in string
    num_characters = total_characters_used(book_text) # returns dictionary of char counts
    sorted_list = book_report(num_characters) # returns sorted list of char count dictionaries
    print_report(book_path, num_words, sorted_list)

    
def print_report(book_path, num_words, sorted_list):
    print(f'''============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
'''+"\n".join(f"{x["char"]}: {x["num"]}" for x in sorted_list)+'''
============= END ===============''')


def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

main()

