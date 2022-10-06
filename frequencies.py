"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newItem = [str(i) for i in items]
    for i in newItem:
        if i not in frequencies:
            frequencies[i] = 1
        else:
            frequencies[i] += 1
    return frequencies
