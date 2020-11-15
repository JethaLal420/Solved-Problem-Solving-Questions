#
#
#
#               FOR Quick USE------------------------------>
#
#
#

def restartGame(n, k):
    return k + n 

def goingBack(n, k, s):
    return (k - s) + (n - s) + k

def startGame(n, k, s):
    sum1 = restartGame(n, k)
    sum2 = goingBack(n, k, s)

    if sum1 > sum2:
        return sum2
    else:
        return sum1

t = int(input())
j = 1
for i in range(0, t):
    tt = input().split()
    n = int(tt[0])
    k = int(tt[1])
    s = int(tt[2])

    result = startGame(n, k, s)
    print('Case #' + str(j) +': ' + str(result))
    j += 1
