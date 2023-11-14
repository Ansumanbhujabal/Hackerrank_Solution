# Determine the factors of a numbers and then return the pth element from the list if there is no pth return 0
# Example if n=20 and p=3
# The factors of 20 are 1,2,4,5,10,20 and if p=3 then 4 will return

import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a = []
        for i in range(1, n+1):
            if n % i == 0:
                a.append(i)
        if len(a) < k:
            return (-1)
        else:
            return (a[k-1])


def findFactor(n, p):
    factors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n / i:
                factors.append(n / i)

    factors.sort()

    if p <= len(factors):
        return factors[p - 1]
    else:
        return 0


# Example usage
n = 20
p = 3
result = findFactor(n, p)
print(result)  # Output: 4
