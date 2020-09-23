chk = [False for _ in range(10001)]

for i in range(1, 10001):
    if chk[i]:
        continue
    print(i)
    num = i
    while True:
        sum = num
        while num > 0:
            sum += num % 10
            num //= 10
        if sum > 10000 or chk[sum]:
            break
        chk[sum] = True
        num = sum