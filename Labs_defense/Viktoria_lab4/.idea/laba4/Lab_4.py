l = 0
r = 0
n = 0
s = 0
N = 0
S = 0
lower_count = 0
upper_count = 0
cooFFicient = 0
char = "#$%@"
password = input("Enter your password: ")
if(len(password)<=4):
    l += 0
elif(len(password)>=5 and len(password)<=7):
    l += 6
elif(len(password)>7 and len(password)<=15):
    l += 12
elif(len(password)>=16):
    l += 18
for i in range(len(password)):
    if password[i].islower():
        lower_count += 1
    elif password[i].isupper():
        upper_count += 1
if lower_count != 0 or upper_count != 0:
    r += 5
elif lower_count != 0 and upper_count !=0:
    r += 7
for i in range(len(password)):
    if password[i].isnumeric():
        N += 1
if N == 1 or N == 2:
    n += 5
elif N >= 3:
    n += 7
for i in char:
    if i in password:
        S += 1
if S == 0:
    s += 0
elif S >= 1 or S <= 2:
    s += 5
elif S > 2:
    s += 10
cooFFicient = l + r + n + s
parameters = [lower_count,upper_count,N,S]
if all(parameters):
    cooFFicient += 6
elif not all(parameters):
    cooFFicient += 4
if cooFFicient<16:
    print("Very easy password")
elif cooFFicient > 15 and cooFFicient < 25:
    print("Easy password")
elif cooFFicient > 24 and cooFFicient < 35:
    print("Middle password")
elif cooFFicient > 34 and cooFFicient < 45:
    print("Strong password")
elif cooFFicient > 44:
    print("Very Strong password")







