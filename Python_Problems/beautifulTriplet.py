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


# Optimized

def beautifulTriplets(d, arr):
    total = sum(1 for i in arr if i+d in arr and i+2 *
                d in arr)  # counts 1 for each element
    return total


print(beautifulTriplets(1, [2, 2, 3, 4, 5]))
