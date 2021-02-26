import re

inputinfo= input('enter name 010-XXXX-XXXX:')
p=re.compile(r'(\w+\s+\d+[-]\d+)[-]\d+')
info = p.search(inputinfo)

print(info.group(1)+'-####')