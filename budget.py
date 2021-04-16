"""
Program for finding ways to use budget.

This code check every cases and find the way to use all the money
"""
#This is the budget you have to spend, item's names you can buy, prices of each of item.
#This is the data for test. After the test it will be replaced with user input. 

from random import randint
budget = randint(110,280) * 100

print('budget for test is $',budget)
item_name = ['PaperBand-aid(1inch)','Coban(1inch)','Coban(2inch)','SkinGuard Band(finger12EA)','AlcoholSwab(Box)','Madecassol(10g)']
item_cost = [1500, 1600, 2400, 3500, 5200, 5400]

#This is number of items you must buy(at least).
item_EA_min =[2, 0, 2, 0, 0, 1]

#If the minimum purchase price exceeds the budget, an error is signaled.
cost_must = 0
for n_budget, n_costchk in enumerate(item_cost):
    cost_must += n_costchk * item_EA_min[n_budget]
    if(cost_must > budget):
        print('ERROR!!!!!!!!!!!!!!!!!!!!!!!!!')

# count the numbers of item.
item_numb = len(item_cost)
print('!!There are', item_numb, 'items.') #Line for debug Monitor.

# calculate maximum EA of each item
item_maxi = []
for n_cost in item_cost:
    item_maxi.append(int(budget / n_cost))
print('!!Maximums are ', item_maxi, 'EA.') #Line for debug Monitor.


# Number of cases for each item (just '+1' for 0 case)
item_case = []
for n, n_maxi in enumerate(item_maxi):
    item_case.append(n_maxi + 1 - item_EA_min[n])
print('!!Numbers of cases: ', item_case) #Line for debug Monitor.

# Calculate number of all cases
case_tot = 1
for n_case in item_case:
    case_tot *= n_case
print('!!There are', format(case_tot, ',d'), 'cases.') #Line for debug Monitor.

#Calculate number of branch cases(number of next case combination). This helps to find each item's EA of each case.
item_branch = []
item_case_temp = item_case
item_case_temp.append(1)
for n_item in range(0, item_numb):
    branch_numb = 1
    n_itemNxt = n_item + 1
    for n_prod in range(n_itemNxt, len(item_case_temp)):
        branch_numb *= item_case_temp[n_prod]
    item_branch.append(branch_numb)
print('!!There are', item_branch, 'branches next of each items.') #Line for debug Monitor.

#check every cases with for loop.
case_list_exact = []
#case_list_about = []
for n_chk in range(0, case_tot):
    case_chk = []   #initiate empty list for set of each case.
    cost_sum = 0    #initiate sum of each case.
    for n_order in range(0, item_numb):
        #With the case index and number of branch cases after the item, It finds how many items should be tested in this turn.
        item_EA = int(n_chk/item_branch[n_order])%item_case[n_order] + item_EA_min[n_order]
        case_chk.append(item_EA)
        cost_sum += (item_EA * item_cost[n_order])
        if cost_sum > budget:
            #if sum is more than budget, breaks the loop and go to next case.
            break
    if cost_sum == budget:
        case_list_exact.append(case_chk)
        #if sum is right append to the list.
    #Kill the code for finding meaningful cases to save memory.
"""
    elif (cost_sum < budget) and ((budget - cost_sum) < min(item_cost)):
        case_list_about.append(case_chk)
"""

print('Founded PERFECT!!!',len(case_list_exact), 'Cases $', budget)
for n_prt in range(item_numb):
    print ('item #', format(n_prt+1,'02d'), format(item_name[n_prt],'27s'),'$', format (item_cost [n_prt],'6,d'))
for n_caseshow in case_list_exact:
    for n_index, n_itemshow in enumerate(n_caseshow):
        print('[#', format(n_index+1,'02d'), ':', format(n_itemshow,'2d'), 'EA]',sep='',end='')
    print('')

"""
____Example for Understanding____

If you have $16
and you should spend all the money
with followings.

apple $5
raspberry $3
grape $8

maximum of each one is
apple 3 EA
raspberry 5EA
grape 2EA

and if we should buy 1grape at least.

cases are
apple     4 (0, 1, 2, 3)
raspberry 6 (0, 1, 2, 3, 4, 5)
grape     2 (1, 2)
so there are 4 * 6 * 2 cases we can check.

then you can check

index 0: apple 0    raspberry 0    grape 1
index 1: apple 0    raspberry 0    grape 2
index 2: apple 0    raspberry 1    grape 1
index 3: apple 0    raspberry 1    grape 2
index 4: apple 0    raspberry 2    grape 1
index 5: apple 0    raspberry 2    grape 2
index 6: apple 0    raspberry 3    grape 1
index 7: apple 0    raspberry 3    grape 2
index 8: apple 0    raspberry 4    grape 1
index 9: apple 0    raspberry 4    grape 2
index10: apple 0    raspberry 5    grape 1
index11: apple 0    raspberry 5    grape 2
index12: apple 1    raspberry 0    grape 1
index13: apple 1    raspberry 0    grape 2
index14: apple 1    raspberry 1    grape 1
index15: apple 1    raspberry 1    grape 2
index16: apple 1    raspberry 2    grape 1
index17: apple 1    raspberry 2    grape 2
index18: apple 1    raspberry 3    grape 1
index19: apple 1    raspberry 3    grape 2
index20: apple 1    raspberry 4    grape 1
index21: apple 1    raspberry 4    grape 2
index22: apple 1    raspberry 5    grape 1
index23: apple 1    raspberry 5    grape 2
index24: apple 2    raspberry 0    grape 1
index25: apple 2    raspberry 0    grape 2
index26: apple 2    raspberry 1    grape 1
index27: apple 2    raspberry 1    grape 2
index28: apple 2    raspberry 2    grape 1
index29: apple 2    raspberry 2    grape 2
index30: apple 2    raspberry 3    grape 1
index31: apple 2    raspberry 3    grape 2
index32: apple 2    raspberry 4    grape 1
index33: apple 2    raspberry 4    grape 2
index34: apple 2    raspberry 5    grape 1
index35: apple 2    raspberry 5    grape 2
index36: apple 3    raspberry 0    grape 1
index37: apple 3    raspberry 0    grape 2
index38: apple 3    raspberry 1    grape 1
index39: apple 3    raspberry 1    grape 2
index40: apple 3    raspberry 2    grape 1
index41: apple 3    raspberry 2    grape 2
index42: apple 3    raspberry 3    grape 1
index43: apple 3    raspberry 3    grape 2
index44: apple 3    raspberry 4    grape 1
index45: apple 3    raspberry 4    grape 2
index46: apple 3    raspberry 5    grape 1
index47: apple 3    raspberry 5    grape 2

There are patterns repeats same number.
apple's pattern size(branches) is 12. (one digit has 12cases)
    6 * 2 * 1(rasp case * grape case*1)
rasp pattern size is 2. 
    2 * 1(case of grape * 1)
grape changes everytime. size 1   

so we can find every combination like this.

item_EA = int(index number / item branch number)%number of each item's cases  + number you should buy at least.

for example

apple in case index 36 is
int(36 / 12) % 4 + 0 = 3

rasp in case index 13 is
int(13 / 2) % 6 + 0 = 0

grape in case index 29 is
int(29 / 1) % 2 + 1 = 2

so we can make every case and check.

and 

apple     $5 * 1 = $5
raspberry $3 * 1 = $3
grape     $8 * 1 = $8

or

apple     $5 * 0 = $5
raspberry $3 * 0 = $3
grape     $8 * 2 = $8

is perfect case.
"""
