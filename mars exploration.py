#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
sa="SOS"
def marsExploration(s):
    a=0
    for i in range(len(s)):
        
        if(s[i]==sa[i%3]):
            pass
        else:
            a=a+1
            
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
