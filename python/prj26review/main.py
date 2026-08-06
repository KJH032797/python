import csv


def csv01():
    with open("test.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows([
            []
        ])

