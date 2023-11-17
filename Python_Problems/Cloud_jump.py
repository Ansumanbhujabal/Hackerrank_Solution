
def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    i = 0
    while True:
        i = (i+k) % n
        # Jumping criteria
        e -= 1
        # For every jump, -1 energy
        if c[i] == 1:
            e -= 2
            # if Thundercloud is present

        if i == 0:
            break
            # If the pointer returns back to original position
    return e


print(jumpingOnClouds(c=[0, 0, 1, 0, 0, 1, 1, 0], k=2))
