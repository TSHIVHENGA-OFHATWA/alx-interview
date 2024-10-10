#!/usr/bin/python3
"""
This module contains the canUnlockAll function that checks if all boxes
in a list of lists can be unlocked given their keys.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each index represents a box and
    contains a list of keys that open other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    if n == 0:
        return True

    visited = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        if current_box not in visited:
            visited.add(current_box)

            for key in boxes[current_box]:
                if key < n and key not in visited:
                    queue.append(key)

    return len(visited) == n
