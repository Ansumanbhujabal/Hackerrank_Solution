
import math
import os
import random
import re
import sys


def squares(a, b):
    i = int(math.ceil(math.sqrt(a)))
    j = int(math.sqrt(b))
    return (j-i+1)


print(squares(24, 49))
