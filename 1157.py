s = input().upper()
arr = []

for i in range(65, 92):
    arr.append(s.count(chr(i)))

num = arr.count(max(arr))
if num > 1:
    print("?")
else:
    print(chr(arr.index(max(arr))+65))