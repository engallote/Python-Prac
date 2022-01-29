import sys


two = list(sys.stdin.readline().rstrip())
thr = list(sys.stdin.readline().rstrip())
res = 0
for i in range(len(two)):
    tmp = two[i]
    two[i] = '0'
    for j in range(len(thr)):
        tmp2 = thr[j]
        for k in range(3):
            thr[j] = str(k)
            num1 = int("".join(two), 2)
            num2 = int("".join(thr), 3)

            if num1 == num2:
                res = num1
        thr[j] = tmp2
    two[i] = '1'
    for j in range(len(thr)):
        tmp2 = thr[j]
        for k in range(3):
            thr[j] = str(k)
            num1 = int("".join(two), 2)
            num2 = int("".join(thr), 3)

            if num1 == num2:
                res = num1
        thr[j] = tmp2
    two[i] = tmp

print(res)