#incompleted

#입력 -> 분석 -> true/false
#0123456789 -> Ture, 9685471230 -> Ture, 6328 -> false, 0112346789 -> false

import re

def DupNums(num):
    p = re.compile(r'\d+\s')
    refnum = p.findall(num)
    result =[]
    for element in refnum:
        cnt=0      
        for n in list(range(0,10)):
            if element.count(str(n))==1: cnt+=1
            else: break                
        if cnt == 10: result.append('Ture')
        else: result.append('False')                
    return ' '.join(result)

if __name__=='__main__':
    inputnum = input('enter the numbers: ')
    #0123456789 01234 01234567890 6789012345 012322456789
    print(DupNums(inputnum))
    #True False False True False