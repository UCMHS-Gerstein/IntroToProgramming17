text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()

def clean_text(text_to_clean): 
    """convert text_to_clean to lowercase and
    strip out punctuation. return the result"""
    clean = ''
    for n in text_to_clean.lower():
        if n not in ',.':
            clean += n
    return clean

def split_words(text_to_split):
    """take a string and return that string
    split into words and sorted alphabetically"""
    words = text_to_split.split()
    words.sort()
    return words

def count_words(list_to_count):
    """take a list of words, and return a
    dictionary of word counts"""
    word_dict = {}
    for word in list_to_count:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def process_text(text_to_process):
    return count_words(split_words(clean_text(text_to_process)))

# clean = clean_text(text)
# word_list = split_words(clean_text(text))

# word_dict = count_words(word_list)

# print(word_dict)

print(process_text("Hello Virendra and Elie. How are you today? Have you seen any eliephants?"))