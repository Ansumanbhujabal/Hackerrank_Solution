#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    max_count_of_num = 0
    for i in arr:
        if arr.count(i) > max_count_of_num:
            max_count_of_num = arr.count(i)
    return (len(arr)-max_count_of_num)


print(equalizeArray([1, 3, 4, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 3, 2]))
