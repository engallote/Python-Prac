import sys
import datetime


N = sys.stdin.readline().rstrip()
N = N[5:]

if '01-20' <= N <= '02-18':
    print("Aquarius")
elif '02-19' <= N <= '03-20':
    print("Pisces")
elif '03-21' <= N <= '04-19':
    print("Aries")
elif '04-20' <= N <= '05-20':
    print("Taurus")
elif '05-21' <= N <= '06-20':
    print("Gemini")
elif '06-21' <= N <= '07-22':
    print("Cancer")
elif '07-23' <= N <= '08-22':
    print("Leo")
elif '08-23' <= N <= '09-22':
    print("Virgo")
elif '09-23' <= N <= '10-22':
    print("Libra")
elif '10-23' <= N <= '11-22':
    print("Scorpio")
elif '11-23' <= N <= '12-21':
    print("Sagittarius")
else:
    print("Capricorn")