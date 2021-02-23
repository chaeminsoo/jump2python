'''
a[0]=even               a[0]=odd

if a[1]=even            if a[1]=odd
append(*a[1])           append(-a[1])

goes on..
'''

def DashInsert(num):
    i=0
    numlist = list(num) #entered str
    newnumlist=[numlist[0]]
    while i < len(numlist)-1:
        refnum1 = int(numlist[i]) #i=0
        refnum2 = int(numlist[i+1])
        
        if refnum1 % 2 == 0 and refnum2 % 2 == 0:
            newnumlist.append('*')
            newnumlist.append(numlist[i+1])
        elif refnum1 % 2 == 1 and refnum2 % 2 == 1:
            newnumlist.append('-')
            newnumlist.append(numlist[i+1])
        else:
            newnumlist.append(numlist[i+1])
        i+=1
    return ''.join(newnumlist)

if __name__ == '__main__':
    inputnum = input('enter a number: ') # ex) 4546793
    reuslt = DashInsert(inputnum)
    print('result: ',reuslt) # ex) 454*67-9-3