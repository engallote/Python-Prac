import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    dic = dict()
    max, name = 0, ""
    for i in range(16):
        a, b, aw, bw = sys.stdin.readline().rstrip().split()
        if int(aw) > int(bw):
            if a in dic:
                dic[a] += 1
                if dic[a] > max:
                    max = dic[a]
                    name = a
            else:
                dic[a] = 1
                if dic[a] > max:
                    max = dic[a]
                    name = a
        else:
            if b in dic:
                dic[b] += 1
                if dic[b] > max:
                    max = dic[b]
                    name = b
            else:
                dic[b] = 1
                if dic[b] > max:
                    max = dic[b]
                    name = b

    print(name)