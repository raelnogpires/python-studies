# exercise 2
# write exercise 1 algorithm in a recursive way.


def count_evens(n: int) -> int:
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 1 + count_evens(n - 1)
    else:
        return count_evens(n - 1)


if __name__ == "__main__":
    print(count_evens(10))
