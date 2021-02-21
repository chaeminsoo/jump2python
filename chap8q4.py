A=[20,55,67,82,45,33,90,87,100,25]

def add50(lis):
    result=0
    for i in lis:
        if i>=50:
            result+=i
    return result

print(add50(A))
