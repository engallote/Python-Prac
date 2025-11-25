import sys


while True:
    N = sys.stdin.readline().rstrip()
    if N == "end":
        break

    if N == "animal":
        print("Panthera tigris")
    elif N == "tree":
        print("Pinus densiflora")
    else:
        print("Forsythia koreana")