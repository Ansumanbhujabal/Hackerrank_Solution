#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    total = 0
    for i in range(0, len(bill)):
        if i != k:
            total += bill[i]
    if b != total/2:
        print(int(b-total/2))
    else:
        print("Bon Appetit")


bonAppetit([3, 10, 2, 9], 1, 12)
