def circularArrayRotation(a, k, queries):
    x = k % len(a)
    a = a[-x:] + a[:-x]
    res = []
    for q in queries:
        res.append(a[q])
    return res


print(circularArrayRotation([3, 4, 5], 4, [1, 2]))
