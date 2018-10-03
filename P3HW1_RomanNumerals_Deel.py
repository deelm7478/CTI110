# CTI-110 
# P3HW1 - Roman Numerals 
# Mathew Deel 
# 10/3/18
#

#User inputs number 1-10
print("Your number will be converted to roman numerals.")
number = int(input("Please enter a number 1 through 10: "))
#Number converted and displayed in roman numeral
if number == 1:
    print("The number",number,"Is equivalent to 'I' in roman numeral form.")
elif number == 2:
    print("The number",number,"Is equivalent to 'II' in roman numeral form.")
elif number == 3:
    print("The number",number,"Is equivalent to 'III' in roman numeral form.")
elif number == 4:
    print("The number",number,"Is equivalent to 'IV' in roman numeral form.")
elif number == 5:
    print("The number",number,"Is equivalent to 'V' in roman numeral form.")
elif number == 6:
    print("The number",number,"Is equivalent to 'VI' in roman numeral form.")
elif number == 7:
    print("The number",number,"Is equivalent to 'VII' in roman numeral form.")
elif number == 8:
    print("The number",number,"Is equivalent to 'VIII' in roman numeral form.")
elif number == 9:
    print("The number",number,"Is equivalent to 'IX' in roman numeral form.")
elif number == 10:
    print("The number",number,"Is equivalent to 'X' in roman numeral form.")
else:
    print("Error. Incorrect input. Try again")
