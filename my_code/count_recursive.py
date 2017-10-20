def count_items(list):
    """
    Return number of items in a list using recursion
    :param list: input list
    :return: number of items in input list
    """
    if not list:
        return 0
    else:
        return 1 + count_items(list[:-1])  # Remove last item from list and add to to number of items


print(count_items(['hello', 1, 4, 2, 'world']))

