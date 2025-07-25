import sys


N, M = sys.stdin.readline().split()
flag = True

for i in N:
    if '0' <= i <= '9':
        continue
    else:
        flag = False

if not flag:
    print("NaN")
else:
    flag = True
    for i in M:
        if '0' <= i <= '9':
            continue
        else:
            flag = False

    if not flag:
        print("NaN")
    else:
        print(int(N) - int(M))