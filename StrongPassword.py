#!/bin/python3
#Hacker Rank Problem
import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special_characters = "!@#$%^&*()-+"
    n=len(password)
    count=0
    if not (any( char.isdigit() for char in password)):
        count += 1
    if not (any( char.islower() for char in password)):
        count += 1
    if not (any( char.isupper() for char in password)):
        count += 1
    if not (any(i in special_characters for i in password)):
        count +=1
    return max(count , 6-n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
