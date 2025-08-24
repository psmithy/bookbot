def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def char_count(book_text):
    char_count_dict = {}
    for i in book_text:
        i = i.lower()
        if i in char_count_dict:
            char_count_dict[i] += 1
        if i not in char_count_dict:
            char_count_dict[i] = 1
    return char_count_dict

def sort_on(char):
    return char["num"]

def sort_char_count(char_count_dict):
    sorted_char_count = []
    for i in char_count_dict:
        sorted_char_count.append({"char": i, "num": char_count_dict[i]})
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count
    