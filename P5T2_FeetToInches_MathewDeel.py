#This converts a number of feet to inches
#11/5/18
#CTI-110 P5T2_FeetToInches
#Mathew Deel
#

#Set the conversion constant
INCHES_PER_FOOT = 12

#Main function
def main():
    #Prompts user for number of feet
    feet = int(input('Enter a number of feet: '))
    #Convert to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')                 

#Formula for conversions
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#Call the main function
main()
