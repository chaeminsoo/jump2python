gu = input('select number among 2 to 9: ')

def gugu(n):
    for i in range(1,10):
        result=int(n)*i
        print(result, end=' ')

if __name__=='__main__':
    gugu(gu)