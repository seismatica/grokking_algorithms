def max_recursive(list):
    """
    Find largest item in a list using recursion
    :param list: list of numbers
    :return: largest number in the list
    """
    if len(list) == 1:
        return list[0]
    elif list[0] < list[1]:
        del list[0]
        return max_recursive(list)
    else:
        del list[1]
        return max_recursive(list)


print(max_recursive([5, 3, 7, 9, 1, 3, 8]))