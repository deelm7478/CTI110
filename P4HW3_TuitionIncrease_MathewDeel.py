# Displays semester tuition amount for next five years
# 10/16/18
# CTI-110 P4HW3 - Tuition Increase
# Mathew Deel
#

def main():
    #Initial cost is established
    semCost = float(8000)
    #Loop started for next 5 years
    for year in range(1,6):
        #New semester cost determined
        semCost *= 1.03
        #Results are printed for that year
        print("For year ",year," the projected semester tuition amount is $",format(semCost,".2f"),sep='')

main()
