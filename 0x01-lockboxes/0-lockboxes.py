#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes

A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened """
    if not boxes:
        return False
    size = len(boxes)
    checker = {}
    index = 0

    for box in boxes:
        if len(box) == 0 or index == 0:
            checker[index] = -1
        for key in box:
            if key < size and key != index:
                checker[key] = key
        if len(checker) == size:
            return True
        index += 1
    return False
