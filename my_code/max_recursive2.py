def max_recursive(list):
    if len(list) == 1:
        return list[0]
    elif list[0] > max_recursive(list[1:]):
        return list[0]
    else:
        return max_recursive(list[1:])


print(max_recursive([5, 3, 7, 9, 1, 3, 8, 10]))