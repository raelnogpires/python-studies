# exercise 4
# create a recursive algorithm to find
# the greatest common divisor (gcd) of two ints


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(5, 8))
    print(gcd(5, 20))
    print(gcd(5, 0))
