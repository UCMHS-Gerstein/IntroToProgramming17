import string

text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()

def clean_text(text_to_clean, forbidden):
    """take a string to clean and a string of forbidden characters.
    print out a version that does not include
    forbidden characters"""
    clean_string = ''
    for letter in text_to_clean:
        if letter not in forbidden:
            clean_string += letter
    return clean_string

def split_string(string_to_split):
    """take a string and return a list of
    the words in that string, sorted alphabetically"""
    words = string_to_split.split()
    words.sort()
    return words

def word_counter(words_to_count):
    """take a list of words and return a 
    dictionary of word quantities"""
    counted = {}
    for word in words_to_count:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    return counted

word_list = split_string(clean_text(text, '.,'))
quantities = word_counter(word_list)
print(quantities)