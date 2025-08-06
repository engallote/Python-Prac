import sys


N = sys.stdin.readline().rstrip()
mo = ['a', 'e', 'i', 'o', 'u']
res, pre = 1, "0"

for i in N:
    if pre == "0":
        if i in mo:
            pre = "mo"
        else:
            pre = "ja"
    elif pre == "mo":
        if i in mo:
            res = 0
            break
        else:
            pre = "ja"
    else:
        if i in mo:
            pre = "mo"
        else:
            res = 0
            break

print(res)