num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

x = num1
y = num2
while y:
    x, y = y, x % y

hcf = x
lcm = (num1 * num2) // hcf

print("\nHCF of",num1,"&",num2,"is",hcf)
print("LCM of",num1,"&",num2,"is",lcm)