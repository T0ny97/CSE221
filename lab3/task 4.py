

def find_mod(a,b,m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 != 0: 
            result = (result * a) % m
        a = (a**2) % m
        b = b//2 
    return result

def rec_func(a, n, m):
    if a == 1:  
        return n % m 
    modds = find_mod(a, n+1, m * (a - 1))  
    s_mod = ((modds - a) // (a - 1)) % m
    return  s_mod

cases = int(input())
for i in range(cases):
    a,n,m = map(int,input().split())
    print(rec_func(a,n,m))

