import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    s_lower = s.lower()
    chars = set(re.findall(r'[a-z]', s_lower))
    allchar = set('abcdefghijklmnopqrstuvwxyz')

    if chars >= allchar:
        return "pangram"
    else:
        return "not pangram"


print(pangrams("The quick brown fox jumps over the lazy dog "))
