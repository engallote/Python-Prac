import math
import sys

N = int(sys.stdin.readline())


def sumNum(num):
    ret = 1
    for a in range(2, num):
        if num % a == 0:
            ret += a

    return ret


for _ in range(N):
    year = int(sys.stdin.readline())
    sumAll = 1
    flag = True
    for i in range(2, year):
        if year % i == 0:
            sumAll += i

            tmp = sumNum(i)
            if tmp > i:
                flag = False
                break

    if year < sumAll and flag:
        print("Good Bye")
    else:
        print("BOJ 2022")
