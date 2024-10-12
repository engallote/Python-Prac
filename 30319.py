import sys


arr = list(map(int, sys.stdin.readline().rstrip().split("-")))

if arr[0] < 2023:
    print("GOOD")
elif arr[0] == 2023 and (arr[1] <= 8 or (arr[1] == 9 and arr[2] <= 16)):
    print("GOOD")
else:
    print("TOO LATE")