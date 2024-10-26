import sys


arr = sys.stdin.readline().split("/")

if 13 <= int(arr[0]):
    print("EU")
elif 13 <= int(arr[1]):
    print("US")
else:
    print("either")