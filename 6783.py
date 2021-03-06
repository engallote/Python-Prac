import sys

N = int(sys.stdin.readline().rstrip())
t, s = 0, 0
for _ in range(N):
    st = sys.stdin.readline().rstrip()
    t += st.count('t')
    t += st.count('T')
    s += st.count('s')
    s += st.count('S')
if t > s:
    print("English")
else:
    print("French")