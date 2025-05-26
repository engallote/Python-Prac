import sys


N = int(sys.stdin.readline())
ak = [[200, 210, 220], [210, 220, 225], [220, 225, 230], [225, 230, 235], [230, 235, 245], [235, 245, 250]]
gr = [[260, 265, 270], [265, 270, 275], [270, 275, 280], [275, 280, 285], [280, 285, 290], [285, 290, 295],
      [290, 295, 300]]
ans1, ans2 = [], []
for i in range(6):
    if ak[i][2] <= N:
        ans1.append(100)
    elif ak[i][1] <= N:
        ans1.append(300)
    elif ak[i][0] <= N:
        ans1.append(500)
    else:
        ans1.append(0)

for i in range(7):
    if gr[i][2] <= N:
        ans2.append(100)
    elif gr[i][1] <= N:
        ans2.append(300)
    elif gr[i][0] <= N:
        ans2.append(500)
    else:
        ans2.append(0)

print(*ans1)
print(*ans2)