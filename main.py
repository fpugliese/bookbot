def main():
    #print_book("books/frankenstein.txt")
    print(count_words("books/frankenstein.txt"))
    

def get_book(path):
    with open ("books/frankenstein.txt") as book:
        book_contents = book.read()
    return(book_contents)

def print_book(path):
    print(get_book(path))

def count_words(path):
    count = 0
    words_number = get_book(path).split()
    for word in words_number:
        count +=1
    return count

main()