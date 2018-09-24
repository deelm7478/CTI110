# A Celsius to Fahrenheit Converter
# 9/24/18
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Mathew Deel
#

#User enters celsius value
celsius = float(input("Enter the temperature in degrees Celsius:"))
                
#Temperature is converted to fahrenheit
fahrenheit = int((9/5 * celsius) + 32)
                
#New fahrenheit temperature is diplayed to user
print("The temperature is",fahrenheit,"degrees fahrenheit")
