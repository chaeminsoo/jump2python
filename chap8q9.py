f1=open('C:/vscpython/sample.txt', 'r')
contents=f1.readlines()
f1.close()

ref = 0
for i in contents:
    ref +=int(i)
aver = ref/len(contents)

#print(ref,'\n',aver)

f2=open('C:/vscpython/result.txt', 'w')
ment1 = 'total: $d' % ref
ment2 = 'average: $d' % aver
f2.write(ment1, ment2)
f2.close()