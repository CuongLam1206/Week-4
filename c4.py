import random
import math
def matrix(n):
    a = [random.uniform(0,10) for i in range(n)]
    b = [random.uniform(0,10) for i in range(n)]
    return a, b
def mae(n,a,b):
    sum=0
    for i in range(n):
        sum+=abs(a[i]-b[i])
    return sum/n
def mse(n,a,b):
    sum=0
    for i in range(n):
        sum+=(a[i]-b[i])**2
    return sum/n
def rmse(n,a,b):
    sum=0
    for i in range(1,n,1):
        sum+=(a[i]-b[i])**2
    return math.sqrt(sum/n)
def Huber_Loss(n,a,b):
    sum=0
    if(abs(a-b)<=0.5):
        for i in range(n):
            sum+=0.5*((a[i]-b[i])**2)
    else:
        for i in range(n):
            sum+=0.5*(abs(a[i]-b[i])-0.5*0.5)
    return sum/n

n = int(input("Nhap num_samples: "))
if(n<=0):
    print("number of samples must be a postive integer number")
else:
    str = input("Nhap ham( MAE| MSE| RMSE| Huber_Loss): ")
    a, b = matrix(n)
    res = 0
    if(str=="MSE"):
        res = mse(n,a,b)
    elif(str=="MAE"):
        res = mae(n,a,b)
    elif(str=="RMSE"):
        res = rmse(n,a,b)
    elif(str=="Huber_Loss"):
        res = rmse(n,a,b)
    else:
        print('loss name loss is not supported')
    if(str=="MSE" or str=="MAE" or str=="RMSE" or str=="Huber_Loss"):
        print(f'Target: {a}')
        print(f'Predict: {b}')
        print(f'{str}: {res}')