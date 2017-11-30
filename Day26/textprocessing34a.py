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

# split text and assign it to split_text
split_text = text_cleaner("""Each January at the Kickoff, a new, challenging game is introduced. These exciting competitions combine
the practical application of science and technology with the fun, intense energy and excitement of a
championship-style sporting event. Teams are encouraged to display Gracious Professionalism® and to
help other teams and cooperate while competing. This is known as Coopertition®.
""").split()
# sort the list
split_text.sort()

# print the list
print(split_text)
