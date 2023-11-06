

import math
import os
import random
import re
import sys


def designerPdfViewer(h, word):
    j = 0
    m = 0
    for i in range(len(word)):
        j = ord(word[i])-97
        for k in range(0, len(h)):
            if h[j] >= m:
                m = h[j]
    print(m*len(word))


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'
designerPdfViewer(h, word)
