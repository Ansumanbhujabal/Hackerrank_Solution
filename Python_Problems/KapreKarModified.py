#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def kaprekarNumbers(p, q):
    lis = []
    for num in range(p, q+1):
        square = str(num**2)

        if square == '1':
            lis.append(num)

        if len(square) > 1:
            right = int(square[-len(str(num)):])
            left = int(square[0:-len(str(num))])

            if right + left == num:
                lis.append(num)

    if lis:
        print(*lis)
    else:
        print('INVALID RANGE')
