import sys


N = int(sys.stdin.readline())
arr = [" @@@   @@@ ", "@   @ @   @", "@    @    @", "@         @", " @       @ ", "  @     @  ",
       "   @   @   ", "    @ @    ", "     @     "]

for _ in range(N):
    print(*arr, sep='\n')