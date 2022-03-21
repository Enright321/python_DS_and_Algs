"""Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd"""

#--------C1-14 - Brute force solution using a generator O(n^2), but you generate all the possibilities
def distinctoddpairgen(array):
    for num1 in array:
        for num2 in array:
            if num1 != num2 and (num1*num2)%2 == 1:
                yield(num1, num2)
                               
data = [1,2,3,4,5,6,7,8,9,10]
gen = distinctoddpairgen(data)
print ('Generator Solution')
for item in gen:
    print (item)
    
#Any two odd numbers will produce an odd product.  O(n)
def determineoddpair(array):
    first_odd = None
    for number in array:
        if number%2 == 1:
            if number!= first_odd and not first_odd is None:    return ('True', first_odd, number)
            else: first_odd = number
    return ('Not found')

data = [2,4]
determineoddpair(data)
  
