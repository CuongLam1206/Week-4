n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

ans = [i for i in a if i in b]

print(ans)