# Capitalize!

import math
import os
import random
import re
import sys
def solve(s):
    name_list = s.split(" ")
    ans_list = []
    
    for i in name_list:
        ans_list.append(i.capitalize())
    # print(ans_list)
    return " ".join(ans_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()