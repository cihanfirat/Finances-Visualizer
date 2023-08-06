print('--------------------------------')
print('----- FINANCIAL VISUALIZER -----')
print('--------------------------------')
#GETTING INPUTS
salary = input('Annual Salary:\n')
housing = input('Monthly Housing:\n')
bills = input('Monthly Bills:\n')
food = input('Weekly Food:\n')
travel = input('Annual Travel:\n')

#CHECKING WHETHER THE GIVEN NUMBERS ARE VALID OR NOT
def invalid(number):
    for i in number:
        if i.isnumeric()==False and i !='.':
            return True
    return False
if invalid(salary) or invalid(housing) or invalid(bills) or invalid(food) or invalid(travel):
    print("Invalid input, please try again.")
else:
    print("All inputs confirmed valid.")
salary  = float(salary)
housing = float(housing)
bills   = float(bills)
food    = float(food)
travel  = float(travel)

#CALCULATING ANNUAL TAX
annual_tax=0
if salary<=10000:
    annual_tax=round(salary*(5/100), 2)
elif salary<=40000:
    annual_tax=round(salary*(10/100), 2)
elif salary<=80000:
    annual_tax=round(salary*(15/100), 2)
else:
    annual_tax=round(salary*(20/100), 2)

#CALCULATING OTHER ANNUAL SPENDS
annual_housing=housing*12
annual_bills=bills*12
annual_food=food*52

#REMAIN CALCULATION
annual_extra=salary - annual_housing - annual_bills - annual_food - travel - annual_tax

#CALCULATING PERCENTAGE OF SPENDS
percentageof_housing=round((annual_housing/salary)*100,2)
percentageof_bills=round((annual_bills/salary)*100,2)
percentageof_food=round((annual_food/salary)*100,2)
percentageof_tax=round((annual_tax/salary)*100,2)
percentageof_travel=round((travel/salary)*100,2)
percentageof_extra=round((annual_extra/salary)*100,2)

#MAKING BAR CHART
width=int(max(percentageof_housing,percentageof_bills,percentageof_food,percentageof_tax,percentageof_travel,percentageof_extra))
line="-----------------------------------" + ("-" * width)
print("\n",line)
print('housing | $ ' + format(annual_housing,'11,.2f')+ ' ' ,end="")
print("| " + format(percentageof_housing,'5,.2f') + '% | ' +("#" * int(percentageof_housing)) )
print('  bills | $ ' + format(annual_bills,'11,.2f') + ' ' ,end="")
print("| " + format(percentageof_bills,'5,.2f') + '% | ' +("#" * int(percentageof_bills)) )
print('   food | $ ' + format(annual_food,'11,.2f') + ' ' ,end="")
print("| " + format(percentageof_food,'5,.2f') + '% | ' +("#" * int(percentageof_food)) )
print(' travel | $ ' + format(travel,'11,.2f') + ' ' ,end="")
print("| " + format(percentageof_travel,'5,.2f') + '% | ' +("#" * int(percentageof_travel)) )
print('    tax | $ ' + format(annual_tax,'11,.2f') + ' ' ,end="")
print("| " + format(percentageof_tax,'5,.2f') + '% | ' +("#" * int(percentageof_tax)) )
print('  extra | $ ' + format(annual_extra,'11,.2f') + ' ' ,end="")
print("| " + format(percentageof_extra,'5,.2f') + '% | ' +("#" * int(percentageof_extra)) )
print(line)




