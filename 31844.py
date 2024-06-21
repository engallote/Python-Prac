import sys

arr = list(sys.stdin.readline())

if arr.index('@') < arr.index('#') < arr.index('!') or arr.index('@') > arr.index('#') > arr.index('!'):
    print(abs(arr.index('@') - arr.index('!')) - 1)
else:
    print(-1)