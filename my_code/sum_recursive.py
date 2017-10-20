def sum_recursive(list):
    """
    Return the sum of all items in a list using recursion
    :param list: list containing numbers
    :return: sum of all items in the list
    """
    if not list:
        return 0
    else:
        return list[0] + sum_recursive(list[1:])


print(sum_recursive([5, 3, 9, 1]))