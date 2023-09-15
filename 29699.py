import sys


N = int(sys.stdin.readline()) - 1
arr = list('WelcomeToSMUPC')

print(arr[N % len(arr)])