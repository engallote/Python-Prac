import sys


arr = {"Algorithm":204, "DataAnalysis":207, "ArtificialIntelligence":302, "CyberSecurity":"B101",
       "Network":303, "Startup":501, "TestStrategy":105}
T = int(sys.stdin.readline())

for _ in range(T):
    str = sys.stdin.readline().rstrip()
    print(arr[str])