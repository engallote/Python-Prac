import sys

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    gold, medal = {}, {}
    for _ in range(N):
        arr = list(sys.stdin.readline().split())
        year = int(arr[0])
        m = arr[2]

        if m == 'Gold':
            if year in gold:
                gold[year] += 1
            else:
                gold[year] = 1

        if year in medal:
            medal[year] += 1
        else:
            medal[year] = 1

    mx, g_year, m_year = 0, 0, 0
    for i in gold.keys():
        if gold[i] > mx or (gold[i] == mx and g_year > i):
            mx = gold[i]
            g_year = i

    mx = 0
    for i in medal.keys():
        if medal[i] > mx or (medal[i] == mx and m_year > i):
            mx = medal[i]
            m_year = i

    print(g_year, m_year)