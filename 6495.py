import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dic = dict()
for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()
    dic[a] = float(b)

for t in range(1, M + 1):
    arr = list(sys.stdin.readline().rstrip().split())
    a, b, left = 0.0, 0, 1
    k = ''
    for i in arr:
        if i == '=' or i == '>' or i == '<' or i == '>=' or i == '<=':
            left = 0
            k = i
            continue

        if i == '+':
            continue

        if i in dic:
            if left == 1:
                a += dic[i]
            else:
                b += dic[i]
        else:
            if left == 1:
                a += float(i)
            else:
                b += int(i)

    a *= 10
    a = round(a)
    b *= 10
    if k == '>':
        if a > b:
            print("Guess #%d was correct." %(t))
        else:
            print("Guess #%d was incorrect." %(t))
    elif k == '<':
        if a < b:
            print("Guess #%d was correct." %(t))
        else:
            print("Guess #%d was incorrect." %(t))
    elif k == '=':
        if a == b:
            print("Guess #%d was correct." %(t))
        else:
            print("Guess #%d was incorrect." %(t))
    elif k == '>=':
        if a >= b:
            print("Guess #%d was correct." %(t))
        else:
            print("Guess #%d was incorrect." %(t))
    else:
        if a <= b:
            print("Guess #%d was correct." %(t))
        else:
            print("Guess #%d was incorrect." %(t))