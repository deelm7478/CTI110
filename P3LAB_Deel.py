# CTI-110 
# P3LAB - Debugging
# Mathew Deel 
# 10/3/18
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    # TO DO: define the rest of the scores

    
    score = float(input('Enter grade: '))

    if score >= 90:
        print("Your grade is: A")
    else:
        if score >= 80:
            print("Your grade is: B")
        else:
            if score >= 70:
                print("Your grade is C")
            else:
                if score >= 60:
                    print("Your grade is: D")
                else:
                    print("Your grade is: F") # TO DO: finish this


# program start
main()
