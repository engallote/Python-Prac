N = int(input())
sum = 0
for i in range(1, N+1):
    if i < 100:
        sum += 1
        continue

    if i // 100 - i % 100 // 10 == i % 100 // 10 - i % 10:
        sum += 1

print(sum)