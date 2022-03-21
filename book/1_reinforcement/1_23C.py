"""
Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don't try buffer overflow attacks in Python!”
"""

def array_index_handler(array, index, value = 100):
    try:
        array[index] = value
        print("New Value set!")
    except IndexError as e:
        print("Don't try buffer overflow attacks in Python!")
array = [1, 2, 3, 4, 5]
array_index_handler(array, 10, 7)
array_index_handler(array, 2, 7)
array_index_handler(array, -1, 27)
array_index_handler(array, -12, 3)
# print (array)