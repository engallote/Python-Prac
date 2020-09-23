A = int(input())
B = int(input())
C = int(input())

res = list(map(int, str(A * B * C)))

for i in range(10):
    print(res.count(i))