N = int(input())
arr = set()

for _ in range(N):
    arr.add(input())

list = list(arr)
list.sort()
list.sort(key=lambda x:len(x))
print(''.join(list))