import sys

N = int(sys.stdin.readline())
ch = {'B': 1, 'S': 2, 'G': 3, 'P': 4, 'D': 5}
st = list(sys.stdin.readline().split())
arr = []
a, b = 0, 0
for i in range(len(st)):
    r = ch[st[i][0]]
    num = int(st[i][1:])
    arr.append((st[i][0], num))

arr.sort(key=lambda x: (ch[x[0]], -x[1]))

for i in range(N):
    if st[i][0] != arr[i][0]:
        print("KO")
        a = arr[i][0]
        b = str(arr[i][1])
        if ch[st[i][0]] > ch[arr[i][0]]:
            print(a + b, st[i])
        else:
            print(st[i], a + b)

        a = -1
        break
    elif st[i][0] == arr[i][0] and int(st[i][1:]) < arr[i][1]:
        a = arr[i][0]
        b = str(arr[i][1])
        print("KO")
        print(a + b, st[i])
        a = -1
        break

if a != -1:
    print("OK")
