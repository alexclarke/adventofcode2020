#!/usr/bin/python3

expenseReport = open('expense-report', 'r')

expenses = expenseReport.readlines()

for firstExpense in expenses:
    firstCost = int(firstExpense.rstrip())
    for secondExpense in expenses:
        secondCost = int(secondExpense.rstrip())
        if firstCost + secondCost < 2020:
            for thirdExpense in expenses:
                thirdCost = int(thirdExpense.rstrip())
                if firstCost + secondCost + thirdCost == 2020:
                    print('Found an answer (' + firstExpense.rstrip() + ', ' + secondExpense.rstrip() + ', ' + thirdExpense.rstrip() + ') EQUAL ' + str(firstCost * secondCost * thirdCost))
                    expenseReport.close()
                    exit()


expenseReport.close()

