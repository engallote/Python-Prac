import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if M - N >= 31:
    print("You are speeding and your fine is $500.")
elif 21 <= M - N <= 30:
    print("You are speeding and your fine is $270.")
elif 1 <= M - N <= 20:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")