#!/usr/bin/python3

import re

programFile = open('input', 'r')
commands = programFile.readlines()

idx = 0
acc = 0

runCommands = {}


while True:
    cmdMatch = re.search('(\w{3}) ([+-]\d+)', commands[idx])
    cmd = cmdMatch.group(1)
    print('Com '+ cmd +' for '+cmdMatch.group(2) )
    if runCommands.get(idx):
        print('BANG '+ str(acc))
        exit()
    else:
        runCommands[idx] = cmd

    if cmd == 'jmp':
        idx += int(cmdMatch.group(2))
    elif cmd == 'acc': 
        acc += int(cmdMatch.group(2))
        idx += 1
    else:
        idx += 1

programFile.close()

