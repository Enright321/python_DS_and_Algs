"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators
"""

# def isEven(k:int):
#   assert type(k) == int, "input must be an integer"
#   return (k & 1 == 0)

def isEven(k:int):
  assert type(k) == int, "Input must be an integer"
  return (k & 1 == 0)

print(isEven(1))
print(isEven(2))
print(isEven('dog'))
