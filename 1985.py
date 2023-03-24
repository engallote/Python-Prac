import sys


def find(n, m):
    for i in range(0, len(m) - 1):
        if 0 < m[i] and m[i + 1] < 9:
            m[i] -= 1
            m[i + 1] += 1

            if m[0] != 0 and equal(n, m):
                return True

            m[i] += 1
            m[i + 1] -= 1

        if m[i] < 9 and 0 < m[i + 1]:
            m[i] += 1
            m[i + 1] -= 1

            if equal(n, m):
                return True

            m[i] -= 1
            m[i + 1] += 1

    return False


def equal(n, m):
    arr1, arr2 = [0 for _ in range(10)], [0 for _ in range(10)]

    for i in n:
        arr1[i] = 1
    for i in m:
        arr2[i] = 1

    for i in range(10):
        if arr1[i] != arr2[i]:
            return False

    return True


for _ in range(3):
    N, M = sys.stdin.readline().rstrip().split()
    N = list(map(int, N))
    M = list(map(int, M))

    if equal(N, M):
        print("friends")
        continue

    flag = find(N, M)

    if flag:
        print("almost friends")
        continue

    if not flag:
        flag = find(M, N)

    if flag:
        print("almost friends")
    else:
        print("nothing")
