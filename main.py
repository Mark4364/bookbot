from stats import words_count, count_char, sort_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")

    book_path = "books/frankenstein.txt"

    print(f"Analyzing book found at {book_path}")

    book = get_book_text(book_path)
    num_words = words_count(book)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_dict = count_char(book)
    #print(char_dict)

    # print the sorted list of dictionaries
    print("--------- Character Count -------")

    new_dict = sort_dict(char_dict)
    for a in new_dict:
        if a['char'].isalpha():
            print(f"{a['char']}: {a['num']}")


main()