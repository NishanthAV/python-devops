list_Of_num = [101,1,22,13,-1,0.4,-2,0,136,89,6]

for i in range(len(list_Of_num)):
        for j in range(len(list_Of_num)):
            if list_Of_num[i] < list_Of_num[j]:
                temp = list_Of_num[i]
                list_Of_num[i] = list_Of_num[j]
                list_Of_num[j] = temp
    
print(list_Of_num)
