#!/usr/bin/python3
""" Module for read_file method """


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: the file to read
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end='')
