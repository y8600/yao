#user input ex1
name=input("please tell me your name")
print("My name is" + name)

# ex2
print("Excecise 2")
drink1= "milk"
drink2= "water"
print("old values:" + drink1 + " and " + drink2)
temdrink=drink1
drink1=drink2
drink2=temdrink
print("New values:" + drink1 + " and " + drink2)
print("\n\n")
#ex3
print("Excercise 3")
Last_name="Liu"
First_name="Yaoyang"
print(f"my name is {Last_name} {First_name}")
#ex4
print("Excecise 4")
num1= 5
num2= 10

print(f"addition of {num1} + {num2}= {num1+num2}")

#ex5
print("Excercise 5")
numbers= [1,2,3,4,5]
print(f"First element: {numbers[0]}")

#ex6
print("Excercise 6")
number=[1,2,3,4,5]
for number in numbers:
    print(number)

#ex7
# Define the number
number = 15
if number >= 10:
    print("The number is greater than or equal to 10.")
else:
    print("The number is less than 10.")

#ex8
def greet(name):
    print(f"Hello, {name}! Welcome!")
greet("yao")

#ex9
# Create a dictionary with three key-value pairs
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict["name"])

#ex10
# Initialize the starting number
i = 1
while i <= 5:
    print(i)
    i += 1

#ex11 Task: Format the following variables into a string: "name", "age", and "city"
# Example output: "John is 30 years old and lives in New York."
name= "yao"
age= 20
city= "Dallas"
print(f"{name} is {age} years old, and study in {city}.")

#ex12 Task: Write a function that takes two numbers and an optional operation (add, subtract, multiply, divide).
# If no operation is provided, it defaults to addition.
def calculate(num1, num2, operation="add"):
    if operation == "add":
        return num1+ num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1/num2

print(calculate(4,7, "add"))

#ex13 Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# Task: Create a list of years [1990, 1991, 1992, 1993, 1994, 1995] and generate a new list with the approximate age of a person born in that year.
# To generate a new list, start with an empty list [], and use append() to add elements to it.
print("Exercise 13:")
years = [1990, 1991, 1992, 1993, 1994, 1995]
current_year = 2024
ages = [current_year - year for year in years]
print(ages)
















