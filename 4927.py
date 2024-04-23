import sys


t = 1
mod = 1000000009
arr = [[0 for _ in range(1001)] for _ in range(1001)]

while True:
    s = sys.stdin.readline().rstrip()
    s = s.replace(".", "")
    if s == '':
        break

    pre = s.split("=")
    numArr = []
    num1, num2, res1, res2 = 0, 0, 0, 0

    if '*' in pre[0]:
        numArr = pre[0].split("*")
        for i in numArr[0]:
            num1 += int(i)
        for i in numArr[1]:
            num2 += int(i)

        res1 = num1 * num2

    else:
        numArr = pre[0].split("+")

        for i in numArr[0]:
            num1 += int(i)
        for i in numArr[1]:
            num2 += int(i)

        res1 = num1 + num2

    for i in pre[1]:
        res2 += int(i)

    res1 %= 9
    res2 %= 9

    if res1 == res2:
        print("%d. PASS" %t)
    else:
        print("%d. NOT!" %t)

    t += 1