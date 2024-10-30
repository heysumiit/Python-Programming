def sum(n):
    if n == 1:
        return 1
    ans = n + sum(n-1)
    return ans

n = int(input("Enter any number :"))
print("Sum from 1 to",n,"is",sum(n))