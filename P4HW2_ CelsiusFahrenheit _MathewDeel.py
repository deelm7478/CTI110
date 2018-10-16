# A table showing Celsius and Fahrenheit temperatures
# 10/16/18
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Mathew Deel
#

def main():
    #Table header is displayed
    print("Celsius\tFahrenheit")
    print("-------------------")
    #Range of celcius temperatures is determined
    for celsius in range(0,21):
        #Fahrenheit is calculated
        fahrenheit = int(9 / 5 * celsius + 32)
        #Both temperatures are displayed
        print(celsius,"\t",fahrenheit)

main()
    
