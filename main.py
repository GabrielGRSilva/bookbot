from stats import count_words, count_characters

def get_book_text (path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def main ():
    text = get_book_text("books/frankenstein.txt")
    count_words("books/frankenstein.txt") #this counts words
    char_number = count_characters(text)
    print (char_number)

main()