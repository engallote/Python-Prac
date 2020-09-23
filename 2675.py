N = int(input())

for i in range(N):
    num, s = input().split()
    num = int(num)

    for j in s:
        print(j*num, end="")
    print()