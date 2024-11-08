n = int(input("Nhap n: "))
x = int(input("Nhap k: "))
a = [int(input(f"Nhap a{i + 1}: ")) for i in range(n)]
a.sort()

l = 0
r = n - 1

while l <= r:
    mid = (l + r) // 2  
    if a[mid] < x:
        l = mid + 1
    else:
        r = mid - 1  

if l < n and a[l] == x:
    print(f'Vị trí cần tìm là {l+1}')
else:
    print('Không tồn tại số k')