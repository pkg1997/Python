def factorial(x):
    if x < 2:
        return 1
    else:
        return (x * factorial(x-1))
num = 8

# to take input from the user
num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is:", result)
