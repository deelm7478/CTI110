#The program lets the user play Rock, Paper, Scissors with the computer
#11/5/18
#CTI-110 P5HW2 - Rock, Paper, Scissors Game
#Mathew Deel
#

#Start main function
def main():
    #import the random tool
    import random
    #assign the computers choices
    comp_choice = random.randint(1, 3)
    #Prompt user for their choice
    choice = input("Choose either rock, paper, or scissors: ")
    #Options if user chose rock
    if choice == "rock":
        if comp_choice == 2:
            print("The computer chose paper. You lose!")
        elif comp_choice == 3:
            print("The computer chose scissors. You win!")
        else:
            print("The result was a tie. Please try again.")
            main()
    #Options if user chose paper        
    elif choice == "paper":
        if comp_choice == 1:
            print("The computer chose rock. You win!")
        elif comp_choice == 3:
            print("The computer chose scissors. You lose!")
        else:
            print("The result was a tie. Please try again.")
            main()
    #Options if user chose scissors
    elif choice == "scissors":
        if comp_choice == 1:
            print("The computer chose rock. You lose!")
        elif comp_choice == 2:
            print("The computer chose paper. You win!")
        else:
            print("The result was a tie. Please try again.")
            main()
    #Program repeats if unknown input
    else:
        print("Please enter your choice exactly as shown")
        main()
main()
