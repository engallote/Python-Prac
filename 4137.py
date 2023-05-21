import sys

T = int(sys.stdin.readline())
dic = dict()
number = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 'G': '4', 'H': '4', 'I': '4',
          'J': '5', 'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6', 'P': '7', 'R': '7', 'S': '7',
          'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9'}

flag = False
for _ in range(T):
    arr = list(sys.stdin.readline().rstrip())
    num = []

    for i in arr:
        if i == '-':
            continue
        if i in number:
            num.append(number[i])
        else:
            num.append(i)

    num.insert(3, '-')
    st = ''.join(num)
    if st in dic:
        dic[st] += 1
        flag = True
    else:
        dic[st] = 1

if flag:
    for i, j in sorted(dic.items()):
        if j == 1:
            continue

        print(i, j)
else:
    print("No duplicates.")