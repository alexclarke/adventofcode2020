#!/usr/bin/python3 

import re
import pprint

class Bag:
    def __init__(self, name, heldBy):
        self.name = name
        self.heldBy = heldBy
    def __repr__(self):
        return str({'name':self.name, 'heldBy':self.heldBy})

def bagsHolding(bag, holdingBag = []):
    print('On '+ str(bag))
    for holder in bag.heldBy:
        if holder.name not in holdingBag:
            holdingBag.append(holder.name)
        bagsHolding(holder, holdingBag)
    return holdingBag


allBags = {}
bags = open('input', 'r')
bagLines = bags.readlines()

for bag in bagLines:

    bagSearch = re.search('^(\w+ \w+) bags contain (.*)$', bag)
    name = bagSearch.group(1)
    if not allBags.get(name): 
        allBags[name] = Bag(name, [])


    for iName in re.findall('\d+ (\w+ \w+) bags?[,.]', bagSearch.group(2)):
        if allBags.get(iName):
            toAdd = allBags[name]
            allBags[iName].heldBy.append(toAdd)
        else:
            allBags[iName] = Bag(iName, [allBags[name]])

holdingShinyGold = bagsHolding(allBags['shiny gold'])

pprint.pprint(holdingShinyGold)
print(str(len(holdingShinyGold)))
