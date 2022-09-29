#!/usr/bin/python3
import sys

def characterize(num):
    tuples = []
    ctr = 0
    l = len(num)
    while ctr < l - 1:
       tuples.append(num[ctr] + num[ctr + 1])
       ctr = ctr + 1
    return tuples

if __name__ == "__main__":
    num = str(sys.argv[1])
    tuples = characterize(num)
    print(tuples)
