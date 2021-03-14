array =[5,7,1,2,0,1,9,6,3,4,8,6,7,9,2,4,1,0,3]

count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')