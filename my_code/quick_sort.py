def quick_sort(list):
    """
    Sort a list using quick sort
    :param list: list of integers
    :return: sort the list using quick sort
    """
    if len(list) < 2:
        return list
    else:
        pivot = list.pop(0)  # Position of pivot actually doesn't matter
        # since all items in list will be compared to pivot anyway
        left = []
        right = []
        for item in list:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return sorted_left + [pivot] + sorted_right


print(quick_sort([5, 13, 7, 9, 1, 10, 8]))
