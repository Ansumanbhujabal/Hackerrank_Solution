

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def camelcase(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return (count+1)


print(camelcase("BlueCleverFox"))
