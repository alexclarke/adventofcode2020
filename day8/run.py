#!/usr/bin/python3

import re

class Command:
    def __init__(self, cmd, value):
        self.cmd = cmd
        self.value = int(value)

programFile = open('input', 'r')
commandLines = programFile.readlines()

commands = {}
i = 0
for line in commandLines:
    cmdMatch = re.search('(\w{3}) ([+-]\d+)', line)
    cmd = cmdMatch.group(1)
    commands[i] = Command(cmd, cmdMatch.group(2))
    i += 1

triedChanging = {}
while True:
    runCommands = {}
    acc = 0
    idx = 0
    print('New run')
    gotAChange = None
    while True:
        if idx == len(commands)-1:
            print('Looks like we made it '+ str(gotAChange))
            print('ACC '+ str(acc))
            exit()

        if runCommands.get(idx):
            break
        else:
            runCommands[idx] = True

        cmd = commands[idx]
        if cmd.cmd == 'jmp':
            if gotAChange or triedChanging.get(idx):
                idx += cmd.value
            else: # No operation
                gotAChange = idx
                triedChanging[idx] = 'jmp'
                idx += 1
        elif cmd.cmd == 'acc': 
            acc += cmd.value
            idx += 1
        else:
            if gotAChange or triedChanging.get(idx):
                idx += 1
            else: # Jump operation
                gotAChange = idx
                triedChanging[idx] = 'nop'
                idx += cmd.value

programFile.close()
