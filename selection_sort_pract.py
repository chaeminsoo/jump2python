import time

start_time = time.time()
array=[7,5,6,9,1,4,2,8,0,3]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
end_time = time.time()
print('time:',end_time-start_time)