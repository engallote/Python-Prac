import sys


arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

a, b = 0, 1.5

a += arr1[0] * 13 + arr1[1] * 7 + arr1[2] * 5 + arr1[3] * 3 + arr1[4] * 3 + arr1[5] * 2
b += arr2[0] * 13 + arr2[1] * 7 + arr2[2] * 5 + arr2[3] * 3 + arr2[4] * 3 + arr2[5] * 2

if a > b:
    print("cocjr0208")
else:
    print("ekwoo")