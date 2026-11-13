"""
MATH 170 - Lab 11: Morse Code
Fall 2026

This is the file that gets graded.

1. Work through lab11.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

def read_code(filename):
    """
    Read a Morse code file into a dictionary: letter -> code,
    e.g. 'A' -> '.-'. The first line of the file is a comment.

    filename : name of the file, e.g. 'morse_code.txt'
    """
    # TODO: your code here
    return None


def encode(text, code):
    """
    The text written in Morse: the codes separated by single spaces,
    and '/' where the text has a space between words.

    text : a string of letters, digits and single spaces
    code : dictionary, letter -> code, as read_code returns it
    """
    # TODO: your code here
    return None


def invert(code):
    """
    A new dictionary that goes the other way: code -> letter,
    e.g. '.-' -> 'A'. The dictionary code is left unchanged.

    code : dictionary, letter -> code
    """
    # TODO: your code here
    return None


def decode(signal, back):
    """
    The text spelled out by the Morse string signal, in capital
    letters, with a space wherever signal has a '/'.

    signal : codes separated by single spaces, '/' between words
    back   : dictionary, code -> letter, as invert returns it
    """
    # TODO: your code here
    return None
