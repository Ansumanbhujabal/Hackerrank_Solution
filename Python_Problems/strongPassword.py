# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
def minimumNumber(n, password):
    upper = digits = lower = special = 0
    for i in password:
        if i.isupper():
            upper += 1
        elif i.isdigit():
            digits += 1
        elif i.islower():
            lower += 1
        elif i in "!@#$%^&*()-+":
            special += 1
    ls = [upper, digits, lower, special]
    # counts checks the number of criteria not fullfilled
    return max(ls.count(0), 6 - n)
