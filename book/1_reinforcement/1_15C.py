"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

def isDistinct(arr):
  number_set = set()
  for i in arr:
    if i in number_set: return False
    else: number_set.add(i)
  return True

print(isDistinct([1, 3, 2, 4, 6]))
print(isDistinct([1, 3, 2, 4, 6, 6]))