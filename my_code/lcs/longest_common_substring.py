def find_longest_substring(str1, str2):
    """
    Find the longest common substring between 2 strings
    :param str1: first string
    :param str2: second string
    :return: longest common substring between 2 input strings
    """
    # Generate array of size len(str1) x len(str2) so length values can be populated later on
    # Array contains all-zero row and column to buffer for i+1 and j+1 index at edge of array
    array = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    # Initialize longest string and its length so they can be updated later on
    longest = 0
    longest_end = 0

    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                array[i+1][j+1] = array[i][j] + 1  # If 2 letters match, add one to cell diagonal below right
                cell = array[i+1][j+1]
                if cell > longest:  # If cell value is higher than current max, update max with cell value
                    longest = cell
                    longest_end = j+1
            else:
                array[i+1][j+1] = 0
    longest_substring = str2[longest_end-longest:longest_end]
    return longest_substring


str1 = 'hish'
str2 = 'fish'
print(f'Longest common substring between {str1} and {str2} is {find_longest_substring(str1, str2)}')