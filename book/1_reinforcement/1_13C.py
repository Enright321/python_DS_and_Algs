"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing"""

def reverseordercopy(array):  #This creates a new array (doesn't change the original)
    length = len(array)
    reversed_array = [None]*length
    for i in range(length):
        reversed_array[length-1-i] = array[i]
    return reversed_array

def reverseorderinplace(a):  #This performs it in place
    i=0
    l = len(a)
    while i<l//2:
        a[i], a[l-1-i] = a[l-1-i], a[i]
        i+=1
    return a

# def reverseorderinplace(a):  #This performs it in place
#     return a[::-1]

data = [2,3,5,7,8,4,3,6,7,4,5]
print(data[::-1])
print(reverseordercopy(data))
print(reverseorderinplace(data))

data = [2,3,5,7,8,4,3,6,7,4]
print(list(reversed(data)))
print(reverseordercopy(data))
print(reverseorderinplace(data))


from timeit import Timer
print(Timer(lambda: reverseordercopy(data)).timeit(), Timer(lambda: reverseorderinplace(data)).timeit(), Timer(lambda: list(reversed(data))).timeit(), Timer(lambda: list(data[::-1])).timeit())