#!/usr/bin/python3

import re

passwordsFile = open('passwords', 'r')

passwords = passwordsFile.readlines()

validCount = 0

def validatePassword(charLowRange, charHighRange, char, password):
    count = 0
    for character in password:
        if character == char:
            count += 1

    if count >= int(charLowRange) and count <= int(charHighRange):
        return True

    return False


for passwordRecord in passwords:
    match = re.match('^(\d+)\-(\d+)\s(\w): (.*)$', passwordRecord)
    charLowRange = match.group(1)
    charHighRange = match.group(2)
    char = match.group(3) 
    password = match.group(4)
    print('Got match with group 1: '+ charLowRange +'-'+ charHighRange +' group 2: '+ char +' group 3: '+ password, )
    if validatePassword(charLowRange, charHighRange, char, password):
        print('Valid!')
        validCount += 1

passwordsFile.close()

print(str(validCount) + ' valid passwords')




