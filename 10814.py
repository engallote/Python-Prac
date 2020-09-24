N = int(input())
dic = {}

for _ in range(N):
    age, name = input().split()
    age = int(age)

    if age in dic.keys():
        dic[age] += "\n" + str(age) + " " + name
    else:
        dic[age] = name

for i in sorted(dic.keys()):
    print(i, dic[i])