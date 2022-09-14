# Find how many of the words in p42_data.txt are triangle words


import pandas as pd

def first_n_tri_num(n):
    return [int(0.5*i*(i + 1)) for i in range(1, n + 1)]

def char_position(letter):
    return ord(letter) - 64

df = list(pd.read_csv("wip\p42_data.txt"))
tri_nums = first_n_tri_num(27) # This is the highest tri number that a word in the file could be

tri_words = []
for word in df:
    word_num = 0
    for char in word:
        word_num = word_num + char_position(char)
    if word_num in tri_nums:
        tri_words.append(word)

print(len(tri_words))