def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # list to hold keys
    # the first item of boxes is already unlocked
    keys = [0]
    # indexes of all items in boxes
    indexList = [i for i in range(len(boxes))]
    # loop through boxes
    for box in boxes:
        # loop through each key in a box for later comparison
        for key in box:
            # loop through length of boxes list to compare index with key
            for i in range(len(boxes)):
                # if box is not current box and key is equal to an index in
                # boxes list, append key to keys list
                if box != boxes[i] and key == i:
                    keys.append(key)
    # check if indexList is equal to unique list of keys, if true,
    # all keys have been found and all boxes can be opened
    return indexList == list(set(keys))
