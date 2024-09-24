#Factorial of number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
       return n*factorial(n-1)
#Input number 
input_number= int(input("Enter a number."))
#calculate the factorial
result= factorial(input_number)
print(f"frictprial of the number is{result}.")
