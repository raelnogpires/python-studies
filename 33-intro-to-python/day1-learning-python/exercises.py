# exercise 1
# create a function that receives two numbers (ints) and returns
# the bigger.

def bigger_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


print(bigger_number(2, 4))
print(bigger_number(15, 9))

# exercise 2
# create a function that receives a list and returns the arithmetic median.


def median(number_list):
    result = 0
    for number in number_list:
        result += number

    return result / len(number_list)


print(median([1, 2, 3, 4, 5, 6]))
print(median([10, 20, 30]))

# exercise 3
# create a function that given x (x > 1) value will print a square of asterisks
# that have x height and x lenght


def stars_square(x):
    if x < 1:
        print("the number must be equal or bigger than 1")

    # loop through the rows
    for i in range(x):
        # print each one of the starts
        for j in range(x):
            print("*", end=" ")
        print()


stars_square(5)

# exercise 4
# create a function that receives a list of names
# and returns the bigger name


def bigger_name(name_list):
    lengthList = []
    for name in name_list:
        lengthList.append(len(name))
        # we append every name length to lengthList

    biggerLength = max(lengthList)  # now we get the max value from lengthList
    lengthIndex = lengthList.index(biggerLength)  # we get the index
    return name_list[lengthIndex]  # and return the name in that index


print(bigger_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))

# exercise 5
# given that 1 liter of paint covers 3 square meters and the paint is selled in
# 18 liters cans and costs R$80,
# create a function that returns two values in a tuple
# the quantity of paint cans and the total price.


def how_many_cans_to_paint_x_square_meters(wallSize):
    liters = wallSize / 3
    cans = liters / 18
    if liters < 18:
        return (liters, 80)
    else:
        return (round(liters), round(cans * 80))


print(how_many_cans_to_paint_x_square_meters(3))
print(how_many_cans_to_paint_x_square_meters(130))

# exercise 6
# create a function that receives 3 sides of a triangle
# and returns the type of the formed triangle (equilateral, isosceles, scalene)
# or "not a triangle" in case is not possible to form a triangle.


def create_triangle(s1, s2, s3):
    is_true = (
        s1 + s2 > s3 and
        s2 + s3 > s1 and
        s1 + s3 > s2
    )

    if not is_true:
        return "not a triangle"
    elif s1 == s2 == s3:
        return "equilateral triangle, three equal sides"
    elif s1 == s2 or s2 == s3 or s1 == s3:
        return "isosceles triangle, two equal sides"
    else:
        return "scalene triangle, three differentes sides"
