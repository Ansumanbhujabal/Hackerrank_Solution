def findDigits(n):
    count = 0
    k = [int(x)for x in str(n)]
    for i in k:
        if n % i == 0:
            count += 1
    return count


print(findDigits(n=124))
