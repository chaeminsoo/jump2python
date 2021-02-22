f1=open('C:/vscpython/abc.txt', 'r')
lines = f1.readlines()
f1.close()

lines.reverse()

f2 = open('C:/vscpython/new_abc.txt','w')
for i in lines:
    f2.write(i)

'''
for i in range(0,len(lines)):
    new_line = lines[len(lines)-1-i]
    f2.write(new_line)'''
f2.close()