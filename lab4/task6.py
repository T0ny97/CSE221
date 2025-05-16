n = int(input())
x, y = map(int,input().split())

valid = []

f1 = False
f2 = False

if y-1>0 or x-1>0:
    if x-1>0 and y-1>0:
        valid.append((x-1,y-1))
    
    if x-1>0:
        valid.append((x-1,y))
    
    if y+1<=n and x-1>0:
        valid.append((x-1,y+1))

    if y-1>0:
        valid.append((x,y-1))
    



if y+1<=n or x+1<=n:

    if y+1<=n: #t
        valid.append((x,y+1))

    if y-1>0 and x+1<=n: #br
        valid.append((x+1,y-1))

    if x+1<=n: #Right
        valid.append((x+1,y))

    if x+1<=n and y+1<=n:
        valid.append((x+1,y+1))


print(len(valid))
for i in valid:
    print(i[0]," ", i[1])
