#Program to find the factorial of a number

#define function
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

x=int(input("Enter a number :"))
result = factorial(x)               #Call the function
print("Factorial of",x,"is:",result)