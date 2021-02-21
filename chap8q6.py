inputlist=input('enter numbers(split them by","): ')

result = 0
for i in inputlist.split(','):
    result += int(i)

print(result)