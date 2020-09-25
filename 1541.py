arr = [sum(map(int, i.split('+'))) for i in input().split('-')]

print(arr[0] - sum(arr[1:]))