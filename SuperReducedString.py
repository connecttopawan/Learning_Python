#!/bin/python3

import math
import os
import random
import re
#Hacker Rank Problem
import sys

# Complete the superReducedString function below.
def superReducedString(s): 
    """if (len(s)<=100 and len(s)>=1):
        count_dict = {}
        for char in s:
            #print(char)
            if (char in count_dict.keys()):
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        new_string=''
        for key in count_dict.keys():
            print(key,count_dict[key])
            if (count_dict[key] % 2 == 1):
                new_string += key
        if (new_string is ''):
            return 'Empty String'
        else:
            return new_string """
    x = []
 
    for c in s:
        if not x:
            x.append(c)
        else:
            if x[-1] == c:
                x.pop()
                print(x)
            else:
                x.append(c)
                print("Else : ",x)
             
    if not x:
        return "Empty String"
    else:
        return ''.join(x)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
