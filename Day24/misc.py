import random

cat = {'spanish': 'gato', 'italian': 'gatto', 'dutch': 'kat', 'yiddish': 'kats', 'hawaiian': 'anu', 'french': 'chat', 'russian': 'kot', 'german': 'katze'}

def translation_function(n):
    for k, v in cat.items():
        (print(f"{k} -- {v}"))

def pick_language(lang):
    print(cat[lang])

pick_language('yiddish')
pick_language('hawaiian')