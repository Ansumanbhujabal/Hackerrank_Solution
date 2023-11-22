

def cutTheSticks(arr):
    result = []
    while len(arr) > 0:
        # Append the number of remaining sticks before each iteration
        result.append(len(arr))

        # Find the minimum length of sticks
        min_length = min(arr)

        # Cut the sticks and discard pieces of the minimum length
        arr = [x - min_length for x in arr if x > min_length]

    return result
