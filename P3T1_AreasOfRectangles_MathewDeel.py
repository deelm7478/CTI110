# CTI-110 
# P3T1 - Areas of Rectangles
# Mathew Deel 
# 10/3/18
#

# Input length and width of rectangle 1
length1 = int(input("Please enter the length of rectangle 1: "))
width1 = int(input("Please enter the width of rectangle 1: "))
# Input length and width of rectangle 2
length2 = int(input("Please enter the length of rectangle 2: "))
width2 = int(input("Please enter the width of rectangle 2: "))
# Calculate the area of rectangles
area1 = length1 * width1
area2 = length2 * width2
#Determine which rectangle has a greater area
if area1 > area2:
    print("Rectangle 1 has the greatest area")
elif area1 < area2:
    print("Rectangle 2 has the greatest area")
else:
    print("Both rectangles have the same area")
