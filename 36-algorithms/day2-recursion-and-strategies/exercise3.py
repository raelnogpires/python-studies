# exercise 3
# create a recursive algorithm that finds
# the bigger int number in a list


def helper(size: int, numbers: list) -> int:
    if size == 1:
        return numbers[0]

    else:
        bigger = helper(size - 1, numbers)
        if bigger > numbers[size - 1]:
            return bigger
        else:
            return numbers[size - 1]


def find_bigger_number(numbers: list) -> int:
    size = len(numbers)
    return helper(size, numbers)


if __name__ == "__main__":
    print(find_bigger_number([1, 21, 300, 4, 57]))
    print(find_bigger_number([27, 5, 198, 86, 153, 201, 75, 360]))
