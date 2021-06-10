# algorithm that show how many time we flip binary zero to one or one to zero at least?

import sys
input = sys.stdin.readline

S = list(map(int, input().rstrip()))

count = 0
current = S[0]


for bi in S:
    if bi != current:
        count += 1
        current = bi

if count % 2 == 0 and count != 0:
    count = count // 2
elif count % 2 == 1 :
    count = count//2 + 1

print(count)