# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    maxSpent = -1
    for i in keyboards:
        for j in drives:
            totalPrice = i+j
            if totalPrice <= b and totalPrice > maxSpent:
                maxSpent = totalPrice
    return (maxSpent)


print(getMoneySpent([10, 2, 3], [5, 2, 8], 31))
