# Calculates the amount a user is above or below his budget
# 10/15/18
# CTI-110 P4HW1 - Budget Analysis
# Mathew Deel
#

def main():
    #Initialize the accumulator
    total = 0

    #Set sentinel value
    sentinel = 0

    #Ask user for budget
    budget = float(input("Please enter your amount budgeted for the month: "))

    #Ask user for first expense
    expense = float(input("Please enter your expenses one at a time or '0' when all expenses entered: "))

    #Expenses for user calculated
    while expense != sentinel:
        
        #Expense is added to accumulator
        total += expense
        print(expense,"has been added to total")
        
        #Ask user for aditional expenses
        expense = float(input("Please enter your expenses one at a time or '0' when all expenses entered: "))

    #Difference in expenses and budget determined
    remainder = budget - total

    #Results are displayed to user
    if remainder > 0:
        print("Your expenses total to " ,total," and are under budget by $",remainder,sep='')
    elif remainder == 0:
        print("Wow, your expenses are exactly on budget")
    elif remainder < 0:
        print("Your expenses total to ",total," and are over budget by $",abs(remainder),sep='')
    else:
        print("Error. Unknown Output. Please restart program.")

main()

