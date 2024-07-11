import sys
import string

N = sys.stdin.readline()
arr = list(string.ascii_uppercase)

for i in N:
    if i in arr:
        arr.remove(i)

print(arr[0])