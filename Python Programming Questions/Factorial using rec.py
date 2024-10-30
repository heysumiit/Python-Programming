def factorial(n):

    if n == 0:
        return 1
         
    return n * factorial(n-1)
while True:
    num = int(input("Enter any Number : "))
    print("Factorial is : ",factorial(num))