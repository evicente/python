#!/usr/bin/env python3
import csv


def open_csv(file_name):
    data = []
    with open (file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row[0])
    return data


def main():
    open_csv("data.csv")


if __name__ == "__main__":
    main()