len, k = map(int,input().split())
arr = list(map(str,input().split()))
output = arr[:k]
output = output[::-1]
print(" ".join(map(str,output)))