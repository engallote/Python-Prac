import sys


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    return gcd(b, a % b)


st = set()
games, words = 0, 0
tmp = []
while True:
    try:
        s = sys.stdin.readline()
        if s == "":
            break

        for i in s:
            if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
                tmp.append(i)
            else:
                if ''.join(tmp) == 'BULLSHIT':
                    words += len(st)
                    st.clear()
                    games += 1
                else:
                    if len(tmp) != 0:
                        st.add(''.join(tmp).lower())
                tmp = []

        if len(tmp) == 0:
            continue
        if ''.join(tmp) == 'BULLSHIT':
            games += 1
            words += len(st)
            st.clear()
        else:
            st.add(''.join(tmp).lower())
    except:
        break

g = gcd(words, games)

print(words // g, '/', games // g)
