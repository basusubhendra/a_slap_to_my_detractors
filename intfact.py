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
    while (ctr == 0) or ((ctr + 1) % l != 0): 
       tuples.append(num[ctr % l] + num[(ctr + 1) % l])
       ctr = ctr + 1
    return tuples

if __name__ == "__main__":
    num = str(sys.argv[1])
    tuples = characterize(num)
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
    ll = len(tuples)
    for x in range(0, 2):
       while True:
           if _pivot_relation_ == _relation_(e_str[0], e_str[1]):
               accumulator = accumulator + 1
               _current_relation_ = _relation_(p_str[0], p_str[1])
               if _current_relation_ == _tuple_relation_:
                   input([tuples[ctr % ll],accumulator])
                   bin_str += bin(accumulator)[2:]
                   ctr = ctr + 1
                   _tuple_relation_ = _relation_(tuples[ctr % ll][0], tuples[ctr % ll][1])
                   accumulator = 0
                   #Roles of pi and e are reversed
                   tt = pp
                   pp = ee
                   ee = tt
                   e_str = str(ee.read(2))
                   p_str = str(pp.read(2))
                   _pivot_relation_ = _relation_(e_str[0], e_str[1])
                   if ctr == len(tuples):
                        factor1 = bin_str
                        bin_str = ""
                        break
                   elif ctr == 2*len(tuples):
                        factor2 = bin_str
                        break
           e_str = str(ee.read(2))
           p_str = str(pp.read(2))
    #TBD Factors to be printed
    #print(factor1)
    #print(factor2)
    pp.close()
    ee.close()
