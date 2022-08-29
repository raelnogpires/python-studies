# exercise 1
# create an non-recursive algorithm that counts
# how many even numbers are present in a certain
# numeric sequence.


def count_evens(number: int) -> int:
    even_count = 0
    for n in range(1, number):
        if n % 2 == 0:
            even_count += 1

    return even_count


print(count_evens(10))
