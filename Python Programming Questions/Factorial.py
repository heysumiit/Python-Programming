while True:
    num = int(input("Enter any Number : "))
    if (num == 0 or num == 1):
        print("Factorial of",num,"is",1)

    else:
        fact = 1
        for i in range(1,num+1):
            fact *= i
        print("Factorial of",num,"is",fact)