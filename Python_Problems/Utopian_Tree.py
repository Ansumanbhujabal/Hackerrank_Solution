def utopianTree(n):
    j = 1
    for i in range(1, n+1):
        if j % 2 == 0:
            j = j+1
        else:
            j = j*2
    return j


print(utopianTree(0))
