# Calculates male and female percentages in a class
# 9/24/18
# CTI-110 P2HW2 - Male Female Percentage
# Mathew Deel
#

#User inputs number of males
male = int(input("Enter the number of male students in the class:"))

#User inputs number of females
female = int(input("Enter the number of female students in the class:"))

#Previous numbers used to calculate total number of students in class
total = male + female

#Male percentage calculated and stored
malePer = int(male / total * 100)

#Female percentage calculated andstored
femalePer = int(female / total * 100)

#Percentages displayed to user
print("The class is",malePer,"percent male and",femalePer,"percent female")
