def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2


print("Please select the operation:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

choice = input("Please enter the choice: ")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if choice == "1":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == "2":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == "3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == "4":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("This is an invalid input")