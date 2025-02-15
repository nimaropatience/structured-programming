
# def f():
#  #local variables 
#   s= "I love sausages"
#   print(s)
# f()  

   

# #Calculating the area of a circle
# #Assigning pi value to variable p
# p = 3.142


# #Capturing the radius value from user
# R =float(input("Enter radius of the circle:"))
# #Computing the area of the circle
# Area = (p*R**2)
# #Displaying the area of the circle
# print(f"The area of the circle is{Area}")


#Calculating the perimeter of a rectangle

# #Capturing length and width from the user
# width=int(input("Enter width of the rectangle:"))
# length=int(input("Enter length of the rectangle:"))

# #Computing the perimeter
# perimeter= 2 *(length + width)
# #Displaying the perimeter
# print(f"The perimeter of the rectangle is{perimeter}")


#Stores marks for 4 Assignments in a list
# Stores marks for 4 assignments in a list
# assignments = []
# for i in range(1,5):
#     mark = float(input(f"Enter the marks for Assignment {i} (out of 100): "))
#     assignments.append(mark)

# #Compute the coursework score (average of the assignments)
# coursework_score = sum(assignments) / len(assignments)

# Display the student's coursework score
#  print(f"The coursework score is: {coursework_score}")

# # Check if the student is allowed to write exams
# if coursework_score >= 35:
#     print("The student is allowed to write exams.")
# else:
#     print("The student is NOT allowed to write exams.")

# Amount = 1000
# def calculate_yaka(yakaunits):
#     return Amount/yakaunits
# result =calculate_yaka(560)
# print(f"The number of yakaunits are{result}")



# Units_consumed = 20
# def amount_paid(cost_unit):
#     return Units_consumed *cost_unit
# result=amount_paid(41000



# def calculate_yaka(amount):
#     return amount / 560

# def amount_paid(units_consumed):
#     return units_consumed * 41000

# def main():
#     # Calculate Yaka Units
#     amount = int(input("Enter amount paid: "))
#     yaka_result = calculate_yaka(amount)
#     # print(f"The number of yaka units are: {yaka_result}")

#     # Calculate Amount Paid
#     units_consumed = int(input("Enter units consumed: "))
#     amount_result = amount_paid(units_consumed)
#     # print(f"The total amount paid is: {amount_result}")


# main()



assignments = []
for i in range(1,5):
    marks =int(input(f"Enter marks for Assignment {i} (out 100);"))
    assignments.append(marks)
    print(assignments)


    work = sum(assignments)/len(assignments)
    print(work)
    









