# exercise 2
# build a class named Statistics
# that calculates the mean, median and mode of a number list

class Statistics:
    def mean(numbers):
        sum = 0
        for number in numbers:
            sum += number

        return sum / len(numbers)

    def median(numbers):
        numbers.sort()
        if len(numbers) % 2 != 0:
            index = round(len(numbers) / 2)
            return numbers[index]
        else:
            index = round(len(numbers) / 2)
            return (numbers[index] + numbers[index + 1]) / 2

    def mode(numbers):
        result = max(set(numbers), key=numbers.count)
        return result


math = Statistics

math.mean([1, 2, 3, 4, 5, 6])
math.mean([10, 9, 8, 7, 6])

math.median([1, 0, 2, 3, 1, 4, 5, 1, 0, 3, 0, 7, 8, 9, 0, 1])

math.mode([10, 30, 50, 10, 50, 80, 50])
