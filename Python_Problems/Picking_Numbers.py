# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    maxCount = 0
    for i in a:
        x = a.count(i)
        y = a.count(i+1)
        x = x+y
        if x > maxCount:
            maxCount = x
    return maxCount


input_list = [4, 5, 5, 6, 6, 6, 7]
result = pickingNumbers(input_list)
print(result)
