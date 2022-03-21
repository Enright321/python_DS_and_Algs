""" Demonstrate how to use pythons list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] """

def sumOfIncTwo():
    a = 0
    factor = 0
    while True:
        yield a
        factor += 1
        a += 2*factor
gen = sumOfIncTwo()
print([next(gen) for _ in range(10)])
