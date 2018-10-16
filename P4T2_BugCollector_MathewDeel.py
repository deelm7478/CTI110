# Collects and displays the number of bugs collected.
# 10/15/18
# CTI-110 P4T2 - Bug Collector
# Mathew Deel
#

def main():
    #Initialize the accumulator
    total = 0

    #Get the bugs collected for each day.
    for day in range(1, 6):
        #Prompt user for amount of bugs that day
        print('Enter the bugs collected on day', day)
        
        #User must input number of bugs
        bugs = int(input())
        
        #Gets the total for the week
        total += bugs

    #Display the total bugs.
    print('You collected a total of', total, 'bugs.')

main()
