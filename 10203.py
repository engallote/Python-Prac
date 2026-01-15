import sys

N = int(sys.stdin.readline())
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    res = s.count('a')
    res += s.count('e')
    res += s.count('i')
    res += s.count('o')
    res += s.count('u')

    print("The number of vowels in %s is %d." %(s, res))