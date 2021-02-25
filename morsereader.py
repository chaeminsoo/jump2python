#incompleted

def morseread(dot):
    morsedic={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H'
    ,'..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q'
    ,'.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
    return morsedic[dot]

#print(morseread('.-'))

morseline = input('enter the morse-code:')
result=[]
index=0
morsewd=''
alpha=''
while index < len(morseline)-1:
    while morseline[index] != ' ':
        alpha + morseline[index]
        index+=1
    morsewd + morseread(alpha)
    if morseline[index] ==' ' and morseline[index+1] ==' ':
        morsewd + ' '
        index +=1
    elif morseline[index] ==' ' and morseline[index+1] !=' ':
        index+1
        alpha=''
        

print(morsewd)
