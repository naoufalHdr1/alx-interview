#!/usr/bin/python3
"""A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of list of int): A list where each index represents a box, and
    the inner lists represent the keys inside that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

    # Number of boxes
    n = len(boxes)

    # A set to track which boxes we have unlocked
    unlocked_boxes = set([0])

    # A stack to track keys we need to process
    keys_to_check = [0]

    # While there are still keys to check
    while keys_to_check:
        current_box = keys_to_check.pop()

        for key in boxes[current_box]:
            if key not in unlocked_boxes and key < n:
                unlocked_boxes.add(key)
                keys_to_check.append(key)

    return len(unlocked_boxes) == n
