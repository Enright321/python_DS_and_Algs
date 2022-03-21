"""
Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return "Lets try Mike".
"""

def remove_punctuation(data, punc = {'.', ',', '!', '?', ':', ';'}):
    new_arr = []
    for char in data:
        if not char in punc: new_arr.append(char)
    return ''.join(new_arr)

def remove_by_deleting(data, punc = {'.', ',', '!', '?', ':', ';'}):
    char_list = list(data)
    for i in reversed(range(len(data))):
        if char_list[i] in punc: del char_list[i]
    return ''.join(char_list)

print('Appending Solution')
print(remove_punctuation('Hello, my name is Mike!!'))
print(remove_punctuation(''))
print(remove_punctuation('.s,dmf.,xcmv.x,cvm.ds,fms.df'))

print('\nDeleting Solution')
print(remove_by_deleting('Hello, my name is Mike!!'))
print(remove_by_deleting(''))
print(remove_by_deleting('.s,dmf.,xcmv.x,cvm.ds,fms.df'))