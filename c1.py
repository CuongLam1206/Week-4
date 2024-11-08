k = int(input("Nhap so k: "))
a = [int(input()) for _ in range(k)]

n = int(input())
m = int(input())
if(m*n>k):
    print('Không tồn tại ma trận')
else:
    index = 0
    ans = []
    for i in range(n):
        matrix=[]
        for i in range(m):
            matrix.append(a[index])
            index+=1
        ans.append(matrix)
print(ans)