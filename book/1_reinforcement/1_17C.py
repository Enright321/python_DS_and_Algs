""" Had we implemented the scale function (page 25) as follows, does it work properly? 

def scale(data, factor):
    for val in data:
        val *= factor
"""

def scale(data, factor):
    for val in data:
        val *= factor
print('Bad Scaling')
data = [1, 2, 3, 4, 5]
print(data)
scale(data, 5)
print(data)

def realScale(data, factor):
    for i in range(len(data)):
        data[i] *= factor
print('\nGood Scaling')
data = [1, 2, 3, 4, 5]
print(data)
realScale(data, 5)
print(data)

"""
Explanation: val *= factor creates a new instance of val, but doesn't change the reference to the original object in the list data[i] changes the reference to element i, which changes the original array
"""