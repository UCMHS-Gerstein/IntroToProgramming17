# initial uncleaned string
text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()

def text_cleaner(text_to_clean):
    """clean text of undesired characters and return a cleaned string"""
    # create empty string to hold cleaned text
    cleaned_text = ''
    # for each character in the string, copy over only the
    # non-forbidden characters into the new string
    for letter in text_to_clean.lower():
        if letter not in '.,':
            cleaned_text += letter
    return cleaned_text

def create_word_list(string_to_split):
    """Take a string and split it into 
    individual words"""
    words = string_to_split.split()
    words.sort()
    return words

# split text and assign it to split_text
s = "Fred is a gigantic cat. He is black and white."

# # clean the string and store it in cleaned_text
# cleaned_text = text_cleaner(s)

# # split into words and store in words
# words = create_word_list(cleaned_text)

words = create_word_list(text_cleaner(s))

print(words)

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)