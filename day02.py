#adventofcode2017
#crushallhumans
#day2
#20171202

import sys

example_arr = []
example_arr.append([5,1,9,5])
example_arr.append([7,5,3])
example_arr.append([2,4,6,8])
example_checksum = 18

example_arr = []
example_arr.append([1364,461,1438,1456,818,999,105,1065,314,99,1353,148,837,590,404,123])
example_arr.append([204,99,235,2281,2848,3307,1447,3848,3681,963,3525,525,288,278,3059,821])
example_arr.append([280,311,100,287,265,383,204,380,90,377,398,99,194,297,399,87])
example_arr.append([7698,2334,7693,218,7344,3887,3423,7287,7700,2447,7412,6147,231,1066,248,208])
example_arr.append([3740,837,4144,123,155,2494,1706,4150,183,4198,1221,4061,95,148,3460,550])
example_arr.append([1376,1462,73,968,95,1721,544,982,829,1868,1683,618,82,1660,83,1778])
example_arr.append([197,2295,5475,2886,2646,186,5925,237,3034,5897,1477,196,1778,3496,5041,3314])
example_arr.append([179,2949,3197,2745,1341,3128,1580,184,1026,147,2692,212,2487,2947,3547,1120])
example_arr.append([460,73,52,373,41,133,671,61,634,62,715,644,182,524,648,320])
example_arr.append([169,207,5529,4820,248,6210,255,6342,4366,5775,5472,3954,3791,1311,7074,5729])
example_arr.append([5965,7445,2317,196,1886,3638,266,6068,6179,6333,229,230,1791,6900,3108,5827])
example_arr.append([212,249,226,129,196,245,187,332,111,126,184,99,276,93,222,56])
example_arr.append([51,592,426,66,594,406,577,25,265,578,522,57,547,65,564,622])
example_arr.append([215,2092,1603,1001,940,2054,245,2685,206,1043,2808,208,194,2339,2028,2580])
example_arr.append([378,171,155,1100,184,937,792,1436,1734,179,1611,1349,647,1778,1723,1709])
example_arr.append([4463,4757,201,186,3812,2413,2085,4685,5294,5755,2898,200,5536,5226,1028,180])

#part 1 = checksum of minmax diff in each row

checksum = 0
for i in example_arr:
    minv = sys.maxint
    maxv = 0
    for j in i:
        if j > maxv:
            maxv = j
        if j < minv:
            minv = j
    print "max {} min {}".format(maxv, minv)
    checksum += (maxv-minv)

print checksum

# answer: 53460, correct first try

print '-----'

#example_arr = []
#example_arr.append([5,9,2,8])
#example_arr.append([9,4,7,3])
#example_arr.append([3,8,6,5])
#example_checksum = 9


#part 2 = checksum of all evenly divisible results in each row

checksum = 0
c = 0
for i in example_arr:
    per_line = 0
    for j in i:
        for k in i:
            if j > k and not j % k:
                checksum += j/k
                per_line += 1
    print "line {} sums {}".format(c, per_line)
    c += 1

print checksum

# answer: 282, correct first try - use the test cases!!


