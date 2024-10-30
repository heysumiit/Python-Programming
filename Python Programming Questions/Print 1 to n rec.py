def print_n(n):
    if n == 0:
        return
    else:
        print_n(n-1)
        print(n)

n = int(input("Enter any number : "))
print(print_n(n))