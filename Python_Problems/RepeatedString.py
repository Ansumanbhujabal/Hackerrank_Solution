#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count_a = s.count('a')
    repeat_full = n//len(s)
    remaining_s = n % len(s)
    repeat_partial = s[:remaining_s].count('a')
    total_count = (count_a*repeat_full)+(repeat_partial)

    return total_count


print(repeatedString(s='aba', n=10))
