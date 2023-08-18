import sys


pre = 0
for i in range(3):
    num = sys.stdin.readline().rstrip()

    if num == 'Fizz':
        pre += 1
    elif num == 'Buzz':
        pre += 1
    elif num == 'FizzBuzz':
        pre += 1
    else:
        pre = int(num) + 1

if pre % 3 == 0 and pre % 5 == 0:
    print("FizzBuzz")
elif pre % 3 == 0 and pre % 5 != 0:
    print("Fizz")
elif pre % 3 != 0 and pre % 5 == 0:
    print("Buzz")
else:
    print(pre)
