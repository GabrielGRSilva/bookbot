def count_words (text):
        with open(text) as f:
            count_words = f.read() ##this reads the book and transforms it into a list
            word_list = count_words.split()
            return len(word_list)

def count_characters (text):
        lowered_characters = text.lower()
        count_dict = {}
        for char in lowered_characters:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        return count_dict

def get_dict_num(num_key):
    return num_key["num"]

def sort_dictionaries (char_number):
    char_number_list = []
    for char, num in char_number.items():
         dict_char_num = {}
         dict_char_num["char"] = char
         dict_char_num["num"] = num
         if char.isalpha():
            char_number_list.append(dict_char_num)
    char_number_list.sort(reverse=True, key=get_dict_num)
    return char_number_list     

  
  
  
  
  
  #  characters={}
   # values={}
    #dict_list=[]
    #for char, num in char_number.items():
     #   characters[char] = char
      #  values[num] = num
       # dict_list.append(characters[char], values[num])
                         
        #dict_list=[characters[char],values[num]]
        
        #dict_list.sort(reverse=True, key=num)
    #return dict_list