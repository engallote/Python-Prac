import sys

N = int(sys.stdin.readline())
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

cnt1, cnt2 = s1.count('w'), s2.count('w')
if cnt1 == cnt2:
    ans = "Good"
    for i in range(N):
        if s1[i] != s2[i]:
            ans = "Its fine"
            break
    print(ans)
else:
    if cnt1 < cnt2:
        print("Manners maketh man")
    else:
        print("Oryang")