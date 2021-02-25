'''
collect string, if there are repeated elements, return number of repeated time
ex) aaabbcccccca -> a3b2c6a1
'''

inputwd = input('enter a word: ') #aaabbcccccca

wdlist = list(inputwd) #[aaabbcccccca]
new_wdlist=[]
index = 0

while True:
    new_wdlist.append(wdlist[index])
    count =1
    n = 1
    try:
        while wdlist[index] == wdlist[index+n]:
            count+=1
            n+=1
    except IndexError:
        pass

    new_wdlist.append(count)
    index += count
    if index >= len(wdlist):
        break

result=''.join(map(str,new_wdlist))
print('result: ',result)