# exercise 4
# read the content from books.json and calculate
# the percentage of every category in comparasion to the
# total amount of books.
# store the categories and their percentages in .csv file.

import csv
import json


def read_json(file):
    return json.load(file)


def count_books_by_category(data):
    categories = {}
    for book in data:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1

    return categories


def define_percentage(book_count, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in book_count.items()
    ]


def write_csv_data(data, header, rows):
    writer = csv.writer(data)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main__":
    # we get a dict of books
    with open("books.json", mode="r") as file:
        books = read_json(file)

    # now we count how many books exists per category
    book_count = count_books_by_category(books)

    total_books = len(books)
    # we define the percentage with the book count and the total books number
    percentage = define_percentage(book_count, total_books)

    header = ["category", "percentage"]
    # and we write our data in the csv file
    with open("report.csv", mode="w") as file:
        write_csv_data(file, header, percentage)
