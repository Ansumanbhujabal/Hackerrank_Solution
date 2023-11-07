def viralAdvertising(n):
    liked = 0
    shared = 5
    total = 0
    for i in range(n):
        liked = abs(int(shared/2))
        shared = int(liked*3)
        total += int(liked)
    return total


print(viralAdvertising(5))
