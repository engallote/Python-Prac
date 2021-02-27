import sys

a, b, c = sys.stdin.readline().split()

if a == "bubble" or a == "tapioka":
    a = ""
if b == "bubble" or b == "tapioka":
    b = ""
if c == "bubble" or c == "tapioka":
    c = ""

res = a + " " + b + " " + c
res = res.rstrip()
res = res.lstrip()

if len(res) == 0:
    print("nothing")
else:
    print(res)