import sys

arr = list(sys.stdin.readline().split())

res = 0
for i in range(int(arr[0])):
    tmp = list(sys.stdin.readline().split())

    word = tmp[0].rstrip()

    if '_' in word:
        word = tmp[0].split('_')

        for j in word:
            if j == arr[1]:
                res += int(tmp[1])
                break
    else:
        if word == arr[1]:
            res += int(tmp[1])

print(res)