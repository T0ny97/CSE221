a,b = map(int,input().split())
mod = 107


result = 1
a = a % mod  

while b > 0:
    if b % 2 != 0: 
        result = (result * a) % mod
    a = (a**2) % mod 
    b = b//2 


print(result)