morsedic={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H'
    ,'..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q'
    ,'.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
w_morsedic={}
for key, value in morsedic.items():
    w_morsedic[value] = key

inputwd = input('enter the message(in capital):')
result=[]
for wd in inputwd.split():
    for alpha in wd:
        result.append(w_morsedic[alpha])
        result.append(' ')
    result.append(' ')
print(''.join(result).rstrip())