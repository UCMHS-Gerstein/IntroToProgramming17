text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()

def remove_chars(string_to_clean, to_remove):
    """remove specified characters from string to clean.
    return the result."""
    clean_string = ''
    for letter in string_to_clean:
        if letter not in to_remove:
            clean_string += letter
    return clean_string

def abc_sort(string_to_split):
    """take a string, split it into words,
    and return an alphabetically sorted list"""
    words = string_to_split.split()
    words.sort()
    return words

def count_words(words_to_count):
    """take a list of words and return a dictionary
    with word counts for each word"""
    word_counts = {}
    for word in words_to_count:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

words = abc_sort(remove_chars(text, ',.'))
counted = count_words(words)
print(counted)