#!/bin/python3

# This is the solution for problem mentioned in
# https://www.hackerrank.com/challenges/big-sorting/problem
import os

if __name__ == '__main__':
    unsorted = []

    n = int(input())
    for _ in range(n):
        unsorted.append(input())

    # 1st try
    # unsorted.sort(key=lambda x: int(x))

    # 2nd try
    # unsorted.sort(key=int)
    
    # 3rd try
    # unsorted = sorted(unsorted, key=int)
    
    # 4th try
    unsorted.sort()        # Sort according to ASCII value
    unsorted.sort(key=len) # Sort according to len

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write('\n'.join(unsorted))
        fptr.write('\n')
