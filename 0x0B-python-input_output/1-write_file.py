#!/usr/bin/python3
""" A function that defines the write operation on python """


def write_file(filename='', text=''):
    """Write a string to a utf8 text file.
        Args:
            filename (str): The name of the file to write.
            text (str); The text to be written into the file.
        Returns:
            The number of character written.
        """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
