import sys


arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

if sum(arr1) > sum(arr2):
    print("Algosia")
elif sum(arr1) < sum(arr2):
    print("Bajtek")
else:
    flag = False
    for i in range(10, -1, -1):
        if arr1.count(i) > arr2.count(i):
            print("Algosia")
            flag = True
            break
        elif arr1.count(i) < arr2.count(i):
            print("Bajtek")
            flag = True
            break

    if not flag:
        print("remis")