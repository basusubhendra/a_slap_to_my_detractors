#!/usr/bin/python3
import sys

def _relation_(x, y):
    x = int(x)
    y = int(y)
    if x == y and x == 0:
        return 5
    elif y == 0:
        return 4
    elif x == 0:
        return 3
    elif x == y:
        return 2
    elif x > y:
        return 1
    elif x < y:
        return 0
    return -1

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
    pp = open("./pi.txt", "r")
    ee = open("./e.txt", "r")
    e_str = str(ee.read(2))
    p_str = str(pp.read(2))
    ctr = 0
    _pivot_relation_ = _relation_(e_str[0], e_str[1])
    _tuple_relation_ = _relation_(tuples[ctr][0], tuples[ctr][1])
    bin_str = ""
    factor1 = ""
    factor2 = ""
    accumulator = 0
    for x in range(0, 2):
       while True:
           input([p_str, e_str])
           if _pivot_relation_ == _relation_(e_str[0], e_str[1]):
               accumulator = accumulator + 1
               _current_relation_ = _relation_(p_str[0], p_str[1])
               if _current_relation_ == _tuple_relation_:
                   print(accumulator)
                   sys.exit(1)
                   bin_str += bin(accumulator)[2:]
                   ctr = ctr + 1
                   e_str = str(ee.read(2))
                   p_str = str(pp.read(2))
                   if ctr == len(tuples):
                        factor1 = bin_str
                        break
                   e_str = str(ee.read(2))
                   p_str = str(pp.read(2))
                   _tuple_relation_ = _relation_(tuples[ctr][0], tuples[ctr][1])
                   _pivot_relation_ = _relation_(e_str[0], e_str[1])
                   accumulator = 0
           e_str = str(ee.read(2))
           p_str = str(pp.read(2))
       tt = pp
       pp = ee
       ee = tt
       _pivot_relation_ = _relation_(e_str[0], e_str[1])
       ctr = 0
    factor2 = bin_str
    print(factor1)
    print(factor2)
