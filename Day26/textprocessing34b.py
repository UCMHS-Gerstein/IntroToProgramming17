text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()

def remove_chars(string_to_clean, to_remove):
    """remove specified characters from string to clean.
    return the result."""
    clean_string = ''
    for letter in string_to_clean:
        if letter not in to_remove:
            clean_string += letter
    return clean_string

words = remove_chars(text, ',.').split()
print(words)
# call the remove_chars function and make sure it works

# cleaned_text = text.lower()

# split_text = cleaned_text.split()

# split_text.sort()

# print(split_text)