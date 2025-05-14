from stats import count_words

def get_book_text (path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def main ():
    text = get_book_text("books/frankenstein.txt")
    return text

count_words("books/frankenstein.txt")   
