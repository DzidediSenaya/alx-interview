#!/usr/bin/python3
"""
Module with function canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents a
        box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """

    if not boxes or not isinstance(boxes, list):
        return False

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    keys_stack = boxes[0]

    while keys_stack:
        current_key = keys_stack.pop()

        if 0 <= current_key < num_boxes and not unlocked_boxes[current_key]:
            unlocked_boxes[current_key] = True
            keys_stack.extend(boxes[current_key])

    return all(unlocked_boxes)


if __name__ == "__main__":
    # Example usage
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
