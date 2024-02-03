"""
Generator function randomWord has as an argument list of words. It should return any random word from this list. Each time words are different until the end of the list is reached. Then words are taken from the initial list again.


For example if 

list = ['book', 'apple', 'word']

books = randomWord(list)

then possible output example 

first call of next(books) returns apple

second call of next(books) returns book

third call of next(books) returns word

fourth call of next(books) returns book
"""

import random

def randomWord(books):
    lst = books
    random.shuffle(lst)
    
    for item in range(len(lst)):
        yield lst[item]
        
    new_lst = books
    random.shuffle(new_lst)
    
    for item in range(len(new_lst)):
        yield new_lst[item]
    
    while True:
        yield None


list = ['book', 'apple', 'word']
books = randomWord(list)


print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))