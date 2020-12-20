#!/usr/bin/python3 

import re
import pprint


class Bag:
    def __init__(self, name, holds):
        self.name = name
        self.holds = holds
    def __repr__(self):
        return str({'name':self.name, 'holds':self.holds})


class BagHolding:
    def __init__(self, bag, count):
        self.bag = bag
        self.count = count

def bagsHolding(bag):
    totalCount = 0
    for held in bag.holds:
        if bagsHolding(held.bag):
            totalCount += (held.count + held.count * bagsHolding(held.bag))
        else:
            totalCount += held.count
    print(bag.name +' contains '+ str(totalCount) +' bags')
    return totalCount


allBags = {}
bags = open('input', 'r')
bagLines = bags.readlines()

for bag in bagLines:

    bagSearch = re.search('^(\w+ \w+) bags contain (.*)$', bag)
    name = bagSearch.group(1)
    if not allBags.get(name): 
        allBags[name] = Bag(name, [])

    for (count, iName) in re.findall('(\d+) (\w+ \w+) bags?[,.]', bagSearch.group(2)):
        if not allBags.get(iName):
            allBags[iName] = Bag(iName, [])
        allBags[name].holds.append(BagHolding(allBags[iName], int(count)))

holdingShinyGold = bagsHolding(allBags['shiny gold'])
print(str(holdingShinyGold))
