def find_longest_subsequence(str1, str2):
    """
    Find the longest common subsequence between 2 strings
    :param str1: first string
    :param str2: second string
    :return: longest subsequence between 2 strings, with unmatched letters as *'s
    """

    array = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    # Initialize longest string and its length so they can be updated later on
    longest = 0
    longest_end = []

    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                array[i+1][j+1] = array[i][j] + 1  # If 2 letters match, add one to cell diagonal below right
                cell = array[i+1][j+1]
                if cell > longest:  # If cell value is higher than current max, update max with cell value
                    longest = cell
                    longest_end = [i+1, j+1]
            else:
                array[i+1][j+1] = max(array[i+1][j], array[i][j+1])

    i, j = longest_end
    longest_subsequence_str1 = ''
    longest_subsequence_str2 = ''
    # Collect common letters until reaching the max number of common letters
    while longest:
        if array[i][j] == array[i-1][j]:
            i -= 1
            longest_subsequence_str1 += '*'
        elif array[i][j] == array[i][j-1]:
            j -= 1
            longest_subsequence_str2 += '*'
        else:
            assert array[i][j] == array[i-1][j-1] + 1
            longest_subsequence_str1 += str1[i-1]
            longest_subsequence_str2 += str2[j-1]
            i -= 1
            j -= 1
            longest -= 1

    # Reverse collected strings to get longest subsequences for each letter
    return longest_subsequence_str1[::-1], longest_subsequence_str2[::-1]


str1 = 'fish'
str2 = 'fosh'
longest_str1, longest_str2 = find_longest_subsequence(str1, str2)
print(f'Longest subsequence between {str1} and {str2}: {longest_str1} ({str1}), or {longest_str2} ({str2})')
