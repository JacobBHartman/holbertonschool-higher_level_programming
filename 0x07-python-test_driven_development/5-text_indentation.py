#!/usr/bin/python3
"""this module makes adds double spacing to a text"""

def text_indentation(text):
    """
    prints a text with 2 new lines after certain characters

    Args:
        text (str): the text

    Returns:
        nothing

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    step = 1
    chrs = ['.', '?', ':']
    for c in range(0, len(text), step):
        step = 1
        if text[c] in chrs:
            print("{:}".format(text[c]), end="")
            print("\n")
        elif text[c-1] in chrs and text[c] == " ":
            pass
        else:
            print("{:}".format(text[c]), end = "")
