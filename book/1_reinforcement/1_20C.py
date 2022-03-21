"""
Python's random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.
"""

import random

# Brute force solution (BAD)
def custom_shuffle(data):
    array = [None]*len(data)
    used_indices = set()
    for i in range(len(data)):
        added = False
        while added == False:
            choice = random.randint(0, len(data) - 1)
            if choice not in used_indices:
                array[choice] = data[i]
                used_indices.add(choice)
                added=True
    return(array)
print ('Bruteforce Solution')
data = [1,2,3,4,5,6,7]
print(custom_shuffle(data))
random.shuffle(data)
print(data)

# Gradual Swap Solution:
def custom_shuffle_inplace(data):
    l = len(data)
    for i in range(l):
        choice = random.randint(0, l-1-i)
        data[choice], data[l-1-i] = data[l-1-i], data[choice]
print('\nIn place Shuffle Method')
data = [1, 2, 3, 4, 5, 6]
custom_shuffle_inplace(data)
print(data)