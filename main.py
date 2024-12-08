def main():
    book = "books/frankenstein.txt"
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(book)} words found in the document")
    list_of_characters = count_characters(book)
    for i in list_of_characters:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")
    print("--- End report ---")

def get_book(path):
    with open (path) as book:
        book_contents = book.read()
    return(book_contents)

def print_book(path):
    print(get_book(path))

def count_words(path):
    count = 0
    words_number = get_book(path).split()
    return len(words_number)

def count_characters(path):
    dict = {}
    book_lowercase = get_book(path).lower()
    for letter in book_lowercase:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    dict_sorted = []
    for i in dict:
        dict_sorted.append({"char": i, "num": dict[i]})
    dict_sorted.sort(reverse=True, key=sort_on)
    return dict_sorted

def sort_on(dict):
    return dict["num"]

main()