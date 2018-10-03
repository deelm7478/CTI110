# CTI-110 
# P3HW2 - Shipping Charges
# Mathew Deel 
# 10/3/18
#

#User enters weight of package
weight = float(input("PLease enter the weight of the package in pounds: "))
#Shipping rate is determined
if weight <= 2:
    ratePer = float(1.5)
elif weight > 2 and weight <= 6:
    ratePer = float(3)
elif weight > 6 and weight <=10:
    ratePer = float(4)
elif weight > 10:
    ratePer = float(4.75)
else:
    print("Error. Unknown shipping rate")
#Total shipping cost is calculated
shipCost = weight * ratePer
#Shipping charge is displayed to user
print("The shipping cost for ",weight," pounds is $"\
      ,format(shipCost,".2f"),".",sep="")
