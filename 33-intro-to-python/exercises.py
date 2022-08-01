# exercise 1
# create a function that receives two numbers (ints) and returns
# the bigger.

def biggerNumber(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


print(biggerNumber(2, 4))
print(biggerNumber(15, 9))

# exercise 2
# create a function that receives a list and returns the arithmetic median.


def median(list):
    result = 0
    for n in list:
        result += n
    return result / len(list)


print(median([1, 2, 3, 4, 5, 6]))
print(median([10, 20, 30]))
