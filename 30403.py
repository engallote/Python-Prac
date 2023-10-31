import sys

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
big = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
small = ['r', 'o', 'y', 'g', 'b', 'i', 'v']

arr2 = {}
for i in arr:
    if i in arr2:
        arr2[i] += 1
    else:
        arr2[i] = 1

cnt1, cnt2 = 0, 0
for i in arr2.keys():
    if i in big:
        cnt1 += 1
    elif i in small:
        cnt2 += 1

if cnt1 < 7 and cnt2 >= 7:
    print("yes")
elif cnt1 >= 7 and cnt2 < 7:
    print("YES")
elif cnt1 >= 7 and cnt2 >= 7:
    print("YeS")
else:
    print("NO!")