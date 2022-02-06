print("\nThe Fibonacci series is a simple concept using 2 numbers.")
print("The first one starts at 0 and the second one starts at 1.")
print("Then, they both add up and the result is a third number.")
print("The third number adds up to the second number to make the fourth ...ect ")

numbers = int(input("\nHow much numbers of the Fibonacci series will show :"))

First_number = 0
Second_number = 1
Total = 0

for i in range(0, numbers):
    print(Total, end = " , ")
    First_number = Second_number
    Second_number = Total
    Total = First_number + Second_number

print("Here are the " +str(numbers)+ " first numbers of the Fibonacci series.")

