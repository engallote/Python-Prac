import sys

N = int(sys.stdin.readline())

if N == 1996 or N == 1997 or N == 2000 or N == 2007 or N == 2008 or N == 2013 or N == 2018:
    print("SPbSU")
elif N == 2006:
    print("PetrSU, ITMO")
else:
    print("ITMO")