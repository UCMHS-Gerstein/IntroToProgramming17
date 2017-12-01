text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()

def clean_text(text_to_clean): 
    """convert text_to_clean to lowercase and
    strip out punctuation. print the result"""
    for n in text_to_clean.lower():
        if n not in ',.':
            print(n, end='')

clean_text(text)

# split_text = cleaned_text.split()

# split_text.sort()

# print(split_text)