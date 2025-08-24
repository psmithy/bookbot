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