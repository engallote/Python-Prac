arr = set()

for i in range(10):
    num = int(input()) % 42
    arr.add(num)

print(len(arr))