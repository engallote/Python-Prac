from itertools import product

N, M = map(int, input().split())
arr = list(map(str, range(1, N + 1)))

print('\n'.join(map(' '.join, product(arr, repeat=M))))