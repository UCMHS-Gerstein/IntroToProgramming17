text = "I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something."

cleaned_text = text.lower()

split_text = cleaned_text.split()

print(sorted(split_text))

for item in split_text:
    print(item)

# words = {'cat': 5}
words = {}
# words['cat'] = 5

temp_words = {'hope': 1, 'year': 3}

print('hope' in temp_words.keys())