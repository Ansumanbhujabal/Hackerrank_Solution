

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    count = {}
    pairNumbers = 0
    for sock in ar:
        if sock in count:
            count[sock] += 1
        else:
            count[sock] = 1
    for sock_count in count.values():
        pairNumbers += sock_count // 2

    return pairNumbers


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(len(ar), ar)
print(result)
