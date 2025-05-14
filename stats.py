def count_words (book):
    with open(book) as f:
        text = f.read()
        word_list = text.split()
    print (f"{len(word_list)} words found in the document")