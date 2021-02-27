import sys

arr = [0, 0]
for _ in range(9):
    name = sys.stdin.readline().rstrip()
    if name == "Lion":
        arr[0] += 1
    else:
        arr[1] += 1


if arr[0] > arr[1]:
    print("Lion")
else:
    print("Tiger")