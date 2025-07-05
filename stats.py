def words_count(book):
    words = book.split()
    num_words = len(words)
    return num_words

def count_char(book):
    char_dict = {}
    for c in book:
        if c.lower() in char_dict:
            char_dict[c.lower()] += 1
        else:
            char_dict[c.lower()] = 1
    return char_dict

def sort_on(item):
    return item['num']

def sort_dict(dict):
    new_list = []
    for element in dict:
        new_list.append({"char": element, "num": dict[element]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list