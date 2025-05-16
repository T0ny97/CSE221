N = int(input())
arr = []
for _ in range(N):
    inp = input().split()
    name = inp[0]
    dest = inp[4]
    time = inp[6]

    arr.append([name, dest, time])


is_sorted = False
for i in range(N - 1):
    for k in range(N - 1 - i):
        name_1, time_1 = arr[k][0] , arr[k][2]
        name_2, time_2 = arr[k+1][0], arr[k+1][2]

        flag= True
        bigger = False

        if len(name_1) <= len(name_2):
            for i in range(len(name_1)):
                if ord(name_1[i]) < ord(name_2[i]): 
                    bigger = False
                    flag= False
                    break
                elif ord(name_1[i]) > ord(name_2[i]): 
                    bigger =  True
                    flag= False
                    break
        else:
            for i in range(len(name_2)):
                if ord(name_1[i]) < ord(name_2[i]): 
                    bigger = False
                    flag= False
                    break
                elif ord(name_1[i]) > ord(name_2[i]): 
                    bigger =  True
                    flag= False
                    break

        if  flag:
            if len(name_1) < len(name_2): 
                bigger = False
                flag= False
            elif len(name_1) > len(name_2): 
                bigger = True
                flag= False

        if  flag:
            if int(time_1[:2]) > int(time_2[:2]): 
                bigger = False
                flag= False
            elif int(time_1[:2]) < int(time_2[:2]): 
                bigger =  True
                flag= False

        if  flag:

            if int(time_1[3:]) > int(time_2[3:]): 
                bigger = False
            elif int(time_1[3:]) < int(time_2[3:]): 
                bigger =  True

        
        
        
        if  bigger:
            is_sorted = True
            temp = arr[k]
            arr[k] = arr[k + 1]
            arr[k + 1] = temp
    if not is_sorted:
        break
for l in range(N):
    print(f'{arr[l][0]} will departure for {arr[l][1]} at {arr[l][2]}')