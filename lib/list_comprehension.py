#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers= [i for i in num_list if i%2 == 0]
    return even_numbers

print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentence_list):
    my_strings=[f"{i}!" for i in sentence_list ]
    return my_strings
    

print (make_exclamation(["Hello", "I'm doing great", "Python is fun"]))