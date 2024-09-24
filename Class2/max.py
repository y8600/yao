
#Input three numbers
number1= float(input("Enter first number:"))
number2= float(input("Enter second number:"))
number3= float(input("Enter thrid number:"))
#caculate the max
if(number1>number3 and number1>number2):
    max=number1
elif(number3>number1 and number3>number2):
    max=number3
else:
    max=number2
print(max)