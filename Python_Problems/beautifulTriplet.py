#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
def beautifulTriplets(d, arr):
    total = []
    for i in arr:
        j = i+d
        if j in arr:
            k = j+d
            if k in arr:
                total.append(i)
                total.append(j)
                total.append(k)
    return len(total)//3


print(beautifulTriplets(1, [2, 2, 3, 4, 5]))
