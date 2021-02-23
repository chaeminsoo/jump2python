f1=open('C:/vscpython/sample.txt', 'r')
contents=f1.readlines()
f1.close()

ref = 0
for i in contents:
    ref +=int(i)
aver = ref/len(contents)


#print(ref,'\n',aver)

f2=open('C:/vscpython/result.txt', 'w')
ment = 'total: %s\naverage: %s' % (ref,aver)
f2.write(ment)
f2.close()