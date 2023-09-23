def countingValleys(steps, path):
    totalPath = 0
    totalValley = 0
    valley = False

    for i in range(0, steps):
        if path[i] == 'D':
            totalPath -= 1
        else:
            totalPath += 1
        if path[i] == 'U' and totalPath == 0:
            if valley:
                totalValley += 1
            valley = False
        elif path[i] == 'D':
            valley = True
    return totalValley


steps = 12
path = "DDUUDDUDUUUD"
print(countingValleys(steps, path))
