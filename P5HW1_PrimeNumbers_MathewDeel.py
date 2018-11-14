#The program lets you determine if a number is prime
#11/5/18
#CTI-110 P5HW1 - Prime Numbers
#Mathew Deel
#

#Start main function
def main():
#Prompt user to enter the number
    print("We will determine if a chosen whole number is prime")
    number = int(input('Enter a number: '))
    #Call test function and print results
    if is_prime(number) == False:
        print("The number",number," is not prime")
    else:
        print("The number",number,"is prime")

#Start prime test
def is_prime(number):
    for i in range(2, number):
        #Determine if each number is divisible
        if (number % i) == 0:
            status = False
        else:
            status = True
        #Return the status of variable
        return status

main()
