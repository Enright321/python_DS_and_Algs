"""Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n."""

# from math import pow

# def sumOfOddSquares(n):
#   sum_of_squares = 0
#   if(n >= 0):    
#     for i in range(1, n):
#       if(i % 2 != 0):
#         sum_of_squares += pow(i, 2)
#   else:
#     return 'Number must be positive'
#   return int(sum_of_squares)

# def sumOfOddSquares(n):
#   sum_of_odd_squares = 0
#   for i in range(n):
#     if(i % 2 != 0):
#       sum_of_odd_squares += i**2
#   return sum_of_odd_squares

print(sumOfOddSquares(10))
# print(sumOfOddSquares(0))
# print(sumOfOddSquares(-1))