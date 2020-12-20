#!/usr/bin/python3 

import re

passports = open('input', 'r')

passportLines = passports.read()

passportRecords = passportLines.split("\n\n")

print('Got '+ str(len(passportRecords)))

valid = 0

for passport in passportRecords:
    matchedFields = re.findall('(\w{3}):', passport)
    print(matchedFields)
    if any('byr' in s for s in matchedFields) and any('iyr' in s for s in matchedFields) and any('eyr' in s for s in matchedFields) and any('hgt' in s for s in matchedFields) and any('hcl' in s for s in matchedFields) and any('ecl' in s for s in matchedFields) and any('pid' in s for s in matchedFields):
        valid += 1


print(valid)
        

    


    


