import sys
input = sys.stdin.readline

S = int(input())
N = 0
s = 0

while (True):
    if s == S:
        break

    elif s > S:
        N -= 1
        break

    N += 1
    s = N*(1+N)/2

print(N)