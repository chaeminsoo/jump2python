import time 

start_time=time.time()
array = [5,7,1,3,9,4,6,2,8,0]

def quick_sort(array):
    if len(array) <=1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
end_time=time.time()
print('time:', end_time-start_time)