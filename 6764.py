import sys


pre = -1
up, down, same = 0, 0, 0
for _ in range(4):
    num = int(sys.stdin.readline())
    if pre == -1:
        pre = num
        continue
    else:
        if pre < num:
            up += 1
        elif pre > num:
            down += 1
        else:
            same += 1
    pre = num

if up != 0 and down == 0 and same == 0:
    print("Fish Rising")
elif up == 0 and down != 0 and same == 0:
    print("Fish Diving")
elif up == 0 and down == 0 and same != 0:
    print("Fish At Constant Depth")
else:
    print("No Fish")