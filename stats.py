def count_words (text):
        with open(text) as f:
            count_words = f.read() ##this reads the book and transforms it into a list
            word_list = count_words.split()
            print (f"{len(word_list)} words found in the document")

def count_characters (text):
        lowered_characters = text.lower()
        count_dict = {}
        for char in lowered_characters:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        return count_dict
