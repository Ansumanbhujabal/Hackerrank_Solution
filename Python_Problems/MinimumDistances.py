#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def minimumDistances(a):
    mindist = len(a)
    distance = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                distance = abs(j-i)
                mindist = min(mindist, distance)
    if mindist == len(a):
        return -1
    else:
        return mindist


print(minimumDistances([3, 2, 1, 2, 3]))
