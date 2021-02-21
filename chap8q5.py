#a[n]=a[n-1]+a[n-2]

def fibo(num):
    fibolist=[0,1]
    
    while True:
        nextnum=fibolist[len(fibolist)-1] +fibolist[len(fibolist)-2]
        if len(fibolist)<int(num): #nextnum<=int(num):
            fibolist.append(nextnum)
        else:
            break       
    
    return fibolist

a=input('enter a number:')
print(fibo(a))