import sys


N = int(sys.stdin.readline())
arr = {"Poblano":1500, "Mirasol":6000, "Serrano":15500, "Cayenne":40000, "Thai":75000, "Habanero":125000}
res = 0
for i in range(N):
    s = sys.stdin.readline().rstrip()
    res += arr[s]

print(res)