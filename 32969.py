import sys


N = sys.stdin.readline()
keyword = ["social", "history", "language", "literacy"]

if any(key in N for key in keyword):
    print("digital humanities")
else:
    print("public bigdata")