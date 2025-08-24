from stats import get_book_text
from stats import word_count
from stats import char_count
from stats import sort_char_count

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    char_count_dict = char_count(book_text)
    sorted_char_count = sort_char_count(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_count:
        if not i["char"].isalpha():
            continue
        else:
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()