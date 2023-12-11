import sys

dic = {"CU": "see you", ":-)": "I’m happy", ":-(": "I’m unhappy", ";-)": "wink", ":-P": "stick out my tongue",
       "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because",
       "TY": "thank-you", "YW": "you’re welcome", "TTYL": "talk to you later"}
while True:
    s = sys.stdin.readline().rstrip()
    if s in dic:
        print(dic[s])
    else:
        print(s)

    if s == "TTYL":
        break