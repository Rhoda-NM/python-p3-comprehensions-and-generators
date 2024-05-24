#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return (evens)

def make_exclamation(sentence_list):
    sentences = [(f"{sentence}!") for sentence in sentence_list]
    return sentences
s = ["I like computers", "I require coffee", "Live long and prosper"]
print(make_exclamation(s))