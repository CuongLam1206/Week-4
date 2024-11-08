n = int(input('Nhập số n: '))
print("Nhập a[]: ")
a = [(input('Nhap: ')) for i in range(n)]
m = int(input('Nhập m: '))
print("Nhập b[]: ")
b = [(input('Nhập: ')) for i in range(m)]
c = []
for i in range(max(n,m)):
    if i < n:
        c.append(a[i])
    if i< m:
        c.append(b[i])
print (c)