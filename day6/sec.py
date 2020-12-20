#!/usr/bin/python3 

import re

decls = open('input', 'r')

declLines = decls.read()

declRecords = declLines.split("\n\n")

count = 0

for decl in declRecords:
    print('decl:'+decl)
    values = []
    for ind in decl.strip().split('\n'):
        print('ind:'+ind)
        vals = set(ind)
        print(vals)
        values.append(vals)
            
    allAns = values[0].intersection(*values[1:len(values)])
    #print(allAns)

    count += len(allAns)
    print(str(len(allAns))+'   -------------------')


print(count)
