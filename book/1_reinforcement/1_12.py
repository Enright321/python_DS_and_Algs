"""Pythons random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function."""
from random import randrange

def randomchoice(data):
    return data[randrange(0, len(data))]
data = [2,3,5,7,8,4,3,6,7,4,5]
for _ in range(400):
    print(randomchoice(data), end = ' ')