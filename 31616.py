import sys


N = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip()

arr = set()
for i in st:
    arr.add(i)

if len(arr) > 1:
    print("No")
else:
    print("Yes")