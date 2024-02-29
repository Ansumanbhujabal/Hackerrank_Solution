#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#
def howManyGames(p, d, m, s):
    count = 0
    while not s < p:  # can mean s>p or s=p  same as s>=p
        s -= p
        new_price = p - d
        p = new_price if new_price > m else m
        count += 1
    return count
