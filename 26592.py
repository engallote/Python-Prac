import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(float, sys.stdin.readline().split())
    a *= 2
    h = a / b

    print("The height of the triangle is %.2f units" %h)