f1=open('C:/vscpython/abc.txt', 'r')
lines = f1.readlines()
f1.close()

new_lines = lines.reverse()

f2 = open('C:/vscpython/new_abc.txt','w')
