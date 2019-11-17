n = int(input("Enter your first number: "))
k = int(input("Enter your second number: "))
t = n & ~ (1<<k)
print(t)