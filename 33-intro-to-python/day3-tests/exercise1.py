# exercise 1
# create a function that returns a number list with this exceptions:
# if the number is divisible by 3, it will show "Fizz"
# if the number is divisible by 5, it will show "Buzz"
# if the number is divisible by 3 and 5, it will show "FizzBuzz"


def number_list_or_fizz_buzz(n):
    result = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


print(number_list_or_fizz_buzz(4))
