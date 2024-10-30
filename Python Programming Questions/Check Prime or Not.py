num = int(input("Enter any number : "))

if num > 1:
    for i in range(2,(num//2)+1):
        if (num % i) == 0:
            print(num,"is not prime number")
            break
    else:
        print(num,"is prime number")
else:
    print(num,"is not prime number")