
import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumStones(arr):
    j = 0
    sum1, sum2 = 0, 0
    for i in range(0,len(arr),2):
        if i < len(arr):
            sum1 = sum1 + arr[i]
        if i+1 < len(arr):
            sum2 = sum2 + arr[i+1]
#         i =+ 2            Doesn't Work. Don't use this type of increment.
        
    if sum1 > sum2:
        return sum2*2
    else:
        return sum1*2
 
if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

    print(result)
