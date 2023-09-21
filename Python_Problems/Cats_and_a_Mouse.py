# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(z-y) == abs(z-x):
        return ("Mouse C")
    if abs(z-y) > abs(z-x):
        return ("Cat A")
    else:
        return ("Cat B")
