from itertools import permutations

N, M = map(int, input().split())
arr = list(map(str, range(1, N + 1)))

print("\n".join(list(map(" ".join, permutations(arr, M)))))