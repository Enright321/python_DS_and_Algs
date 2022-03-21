"""
Write a short Python function that counts the number of vowels in a given character string.
"""
def vowel_counter(data, vowels = {'a', 'e', 'i', 'o', 'u'}):
    l_data = data.lower()
    counter = 0
    for char in l_data:
        if char in vowels: counter += 1
    return counter

print(vowel_counter('abcdefghijklmnopqrstuvwxyz'))
print(vowel_counter('kdsjfldskfjl'))