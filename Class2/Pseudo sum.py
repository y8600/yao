#Pseudo Input two numbers
number1= float(input("Enter first number:"))
number2= float(input("Enter second number:"))
#calculate the sum
sum_result= number1+ number2
#print the result
print("The sum is:",sum_result)

#Input three numbers
#float(input("Enter first number:"))
number1=7
#float(input("Enter second number:"))
number2=8
#float(input("Enter thrid number"))
number3=4
#caculate the max

if(number1>number2 and number1>number3):
    max=number1
elif(number2>number1 and number2>number3):
    max=number2
else:
    max=number3
print(max)