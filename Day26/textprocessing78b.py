import string

text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something.".lower()
cleaned_text = ''

for letter in text:
    if letter not in string.punctuation:
        cleaned_text += letter

split_text = cleaned_text.split()
split_text.sort()

print(split_text)
