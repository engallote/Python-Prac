import sys

no = []
while True:
    arr = list(sys.stdin.readline().rstrip().split())

    if float(arr[0]) < 0:
        break

    a = float(arr[0])
    b = float(arr[2])

    name = ""
    for i in range(3, len(arr)):
        name += arr[i]
        name += " "
    if a == 0:
        no.append(name.rstrip())
    else:
        res = a / b * 100.0

        if res < 1:
            no.append(name.rstrip())
            continue

        print("%s %0.1f %s %0.0f%%" %(name.rstrip(), float(arr[0]), arr[1], res))

if len(no) != 0:
    print("Provides no significant amount of:")
    for i in no:
        print(i)
