
#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    front = int(p/2)
    if n % 2 == 1:
        back = int(((n-p)/2))
    else:
        back = int(((n-p+1)/2))

    return min(front, back)
