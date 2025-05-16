from stats import count_words, count_characters, sort_dictionaries

def get_book_text (path):                ##Receives the text to be used in other functions
    with open(path) as f:                
        book_text = f.read()
        return book_text

def main ():
    text = get_book_text("books/frankenstein.txt")
    number_of_words = count_words("books/frankenstein.txt")
    char_number = count_characters(text)         
    value_of_chars = sort_dictionaries(char_number)
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print (f"Found {number_of_words} total words")
    print ("--------- Character Count -------")
    for x in value_of_chars:
        print(f"{x['char']}: {x['num']}")
    print ("============= END ===============")


main()