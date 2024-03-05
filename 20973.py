import sys

arr = list(sys.stdin.readline().rstrip())
word = list(sys.stdin.readline().rstrip())

cnt, idx = 0, 0
while idx < len(word):
    cnt += 1
    for i in range(len(arr)):
        if word[idx] == arr[i]:
            idx += 1

        if idx >= len(word):
            break

print(cnt)