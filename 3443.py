import sys

dic = dict()
dic['Kamen'] = 'Rock'
dic['Nuzky'] = 'Scissors'
dic['Papir'] = 'Paper'

dic['Rock'] = 'Rock'
dic['Scissors'] = 'Scissors'
dic['Paper'] = 'Paper'

dic['Pierre'] = 'Rock'
dic['Ciseaux'] = 'Scissors'
dic['Feuille'] = 'Paper'

dic['Stein'] = 'Rock'
dic['Schere'] = 'Scissors'
dic['Papier'] = 'Paper'

dic['Ko'] = 'Rock'
dic['Koe'] = 'Rock'
dic['Ollo'] = 'Scissors'
dic['Olloo'] = 'Scissors'
dic['Papir'] = 'Paper'

dic['Sasso'] = 'Rock'
dic['Roccia'] = 'Rock'
dic['Forbice'] = 'Scissors'
dic['Carta'] = 'Paper'
dic['Rete'] = 'Paper'

dic['Guu'] = 'Rock'
dic['Choki'] = 'Scissors'
dic['Paa'] = 'Paper'

dic['Kamien'] = 'Rock'
dic['Nozyce'] = 'Scissors'

dic['Piedra'] = 'Rock'
dic['Tijera'] = 'Scissors'
dic['Papel'] = 'Paper'

l, r, t = 0, 0, 1
name1, name2 = "", ""
while True:
    tmp = sys.stdin.readline()

    if tmp[0] == '-' or tmp[0] == '.':
        print("Game #%d:" %t)
        if l == 1:
            print(f"{name1}: {l} point")
        else:
            print(f"{name1}: {l} points")
        if r == 1:
            print(f"{name2}: {r} point")
        else:
            print(f"{name2}: {r} points")

        if l > r:
            print(f"WINNER: {name1}")
        elif l < r:
            print(f"WINNER: {name2}")
        else:
            print("TIED GAME")
        print()
        name1 = ""
        name2 = ""
        l, r = 0, 0
        t += 1

        if tmp[0] == '.':
            break
        continue

    if len(name1) == 0:
        code1, a = tmp.rstrip().split()
        code2, b = sys.stdin.readline().rstrip().split()
        name1 = a
        name2 = b
        continue

    lm, rm = tmp.split()
    ap = dic[lm]
    bp = dic[rm]

    if ap == "Rock":
        if bp == "Paper":
            r += 1
        elif bp == "Scissors":
            l += 1
    elif ap == "Scissors":
        if bp == "Paper":
            l += 1
        elif bp == "Rock":
            r += 1
    elif ap == "Paper":
        if bp == "Scissors":
            r += 1
        elif bp == "Rock":
            l += 1