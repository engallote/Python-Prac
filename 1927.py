import sys
from queue import PriorityQueue


N = int(sys.stdin.readline())
arr = PriorityQueue()

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if arr.qsize() == 0:
            print(0)
        else:
            print(arr.get())
    else:
        arr.put(num)
