import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    result.append(int(input()))

# result.sort(reverse=True)
result.reverse()

max = 0

for i in range(n):
    if max < (i+1) * result[i]:
        max = (i+1) * result[i]

print(max)