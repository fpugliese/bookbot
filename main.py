def main():
    book = "books/frankenstein.txt"
    #print_book(book)
    #print(count_words(book))
    print(count_characters(book))
    

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
    return dict

main()