def fac(num):
    if num <= 1:
        return 1

    return num * fac(num - 1)


N = int(input())
res = fac(N)
print(res)