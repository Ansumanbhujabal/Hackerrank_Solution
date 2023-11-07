def beatifulDay(i, j, k):
    count = 0
    for m in range(i, j+1):
        result = int(str(m)[::-1])
        val = abs(result - m)

        if val % k == 0:
            count += 1

    return count


print(beatifulDay(20, 23, 6))
