import sys


N = int(sys.stdin.readline())
arr = [" @@@   @@@ ", "@   @ @   @", "@    @    @", "@         @", " @       @ ",
       "  @     @  ", "   @   @   ", "    @ @    ", "     @     "]

for i in range(9):
    for k in range(N):
        print(arr[i], end=' ')
    print()