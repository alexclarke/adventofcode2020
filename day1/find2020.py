#!/usr/bin/python3

expenseReport = open('expense-report', 'r')

expenses = expenseReport.readlines()

for expense in expenses:
    cost = int(expense.rstrip())
    if cost >= 0 and cost <= 2000:
        for otherExpense in expenses:
            otherCost = int(otherExpense.rstrip())
            totalCost = cost + otherCost
            if totalCost == 2020:
                print('Got ' + str(cost) + ' ', end='')
                print('With ' + str(otherCost) + ' ', end='')
                print('SUM ' + str(totalCost))
                print('Total is ' + str(cost * otherCost))
                exit()

expenseReport.close()

