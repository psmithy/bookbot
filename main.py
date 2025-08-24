from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    wc = word_count(book_text)
    print(f"{wc} words found in the document")

main()