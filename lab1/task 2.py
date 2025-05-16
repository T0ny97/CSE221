n = int(input())
for i in range(n):
    exp = input().split(" ")
    if exp[2]=="+":
        print(f"{int(exp[1]) + int(exp[3])}")
    elif exp[2]=="-":
        print(f"{int(exp[1]) - int(exp[3])}")
    elif exp[2]=="*":
        print(f"{int(exp[1]) * int(exp[3])}")
    elif exp[2]=="/":
        print(f"{int(exp[1]) / int(exp[3])}")
