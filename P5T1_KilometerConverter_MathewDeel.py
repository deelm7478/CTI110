#Prompts user to enter distance in kilmoters and outputs it in miles
#11/5/18
#CTI-110 P5T1_KilometerConverter
#Mathew Deel
#

#Get the number to multiply by
CONVERSION_FACTOR = 0.6214

#Start the main funtion
def main():
    #Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))
    #Display the converted distance.
    show_miles(kilometers)
    
#Start the callback conversion function
def show_miles(km):
    #Formula for conversion 
    miles = km * CONVERSION_FACTOR
    #Output converted miles
    print(km, 'kilometers equals', format(miles,".2f"), 'miles.')

#Calls back the main funtion
main()
