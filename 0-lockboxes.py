#!/usr/bin/python3
"""Lock boxes."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
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


if __name__ == "__main__":
    """Sample Test cases"""
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

    boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
