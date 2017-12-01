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

words = clean_text(text, 'aeiou').split()
print(words)

# cleaned_text = ''

# split_text = cleaned_text.split()
# split_text.sort()

# print(split_text)
