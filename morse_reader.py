morsedic={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H'
    ,'..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q'
    ,'.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}

morseline = input('enter the morse-code:')
morselist = list(morseline)
result=[]
index=0
alpha=''
while index < len(morseline):
    if morseline[index] =='.' or morseline[index] =='-':
        alpha = alpha + morseline[index]
        index += 1
    elif morseline[index] ==' ' and morseline[index-1] != ' ':
        result.append(morsedic[alpha])
        alpha=''
        index +=1
    elif morseline[index] == ' ' and morseline[index-1] ==' ':
        result.append(' ')
        index +=1
result.append(morsedic[alpha])
print(''.join(result))