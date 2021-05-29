import sys

st1 = sys.stdin.readline().rstrip()
st2 = sys.stdin.readline().rstrip()
arr = set()

idx = 0
for i in range(len(st2)):
    if idx < len(st1) and st1[idx] != st2[i]:
        arr.add(st2[i])
    elif idx >= len(st1):
        arr.add(st2[i])
    else:
        idx += 1

print(''.join(arr))