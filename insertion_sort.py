import time

start_time = time.time()
array=[8,6,4,7,2,3,9,1,0]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] =array[j-1], array[j]
        else: break

print(array)
end_time = time.time()
print('time:', end_time-start_time)