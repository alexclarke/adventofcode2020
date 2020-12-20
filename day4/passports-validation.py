#!/usr/bin/python3 

import re

def inRng(value, low, high):
    if value:
        return low <= int(value) <= high
    return False

def validateHeight(value):
    if value:
        if value.endswith('cm'):
            cm = value.replace('cm', '')
            return 150 <= int(cm) <= 193
        elif value.endswith('in'):
            inch = value.replace('in', '')
            return 59 <= int(inch) <= 76
        else:
            return False
    return False

def validateHairColour(value):
    if value:
        return re.search('#[abcdef\d]{6}', value)
    return False

def validateEyeColour(value):
    return value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth'

def validatePassportId(value):
    if value:
        return re.search('^\d{9}$', value)
    return False

passports = open('input', 'r')

passportLines = passports.read()

passportRecords = passportLines.split("\n\n")

print('Got '+ str(len(passportRecords)))

valid = 0

for passport in passportRecords:
    print('\n\n')
    values = {}
    matchedFields = re.findall('(\w{3}:[^\s]+)', passport.replace('\n', ' '))
    for field in matchedFields:
        nameAndValue = field.split(":")
        values[nameAndValue[0]] = nameAndValue[1]

    print(values)
        
    if (
            inRng(values.get('byr'), 1920, 2002) and 
            inRng(values.get('iyr'), 2010, 2020) and 
            inRng(values.get('eyr'), 2020, 2030) and 
            validateHeight(values.get('hgt')) and 
            validateHairColour(values.get('hcl')) and 
            validateEyeColour(values.get('ecl')) and 
            validatePassportId(values.get('pid'))
            ):
        print('VALID!!!!!')
        valid += 1

print(valid)

        




    


    


