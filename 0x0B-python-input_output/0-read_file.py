#!/usr/bin/python3
""" Defines a file reading operation """


def read_file(filename=""):
    '''Print the contents of a utf8 file to stdout'''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
