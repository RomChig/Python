char = "#$%@"
password = input()
while(len(password)<=4):
    print("Your password is very easy, it's length must be > 4 symbols/letters etc, try again")
    password = input()
def check_length(password):
    cl = 0
    if(len(password)<=4):
        cl = 0
    elif(len(password)>=5 and len(password)<=7):
        cl += 6
    elif(len(password)>=7 and len(password)<=15):
        cl += 12
    elif(len(password)>=16):
        cl += 18
    return cl
cl = check_length(password)

def check_register(password):
    cr = 0
    lower_count = 0
    upper_count = 0
    for i in range(len(password)):
        if password[i].islower():
            lower_count+=1
        elif password[i].isupper():
            upper_count+=1
    if lower_count!= 0 or upper_count!= 0:
        cr+=5
    elif lower_count!=0 and upper_count!=0:
        cr+=7
    return cr, lower_count,upper_count
cr,lower_count,upper_count = check_register(password)

def check_numeral(password):
    N = 0
    cn = 0
    for i in range(len(password)):
        if password[i].isnumeric():
            N+=1
    if N == 1 or N == 2:
        cn+=5
    elif N >= 3:
        cn+=7
    return cn,N
cn, N = check_numeral(password)

def check_super_symbol(password,char):
    S = 0
    cs = 0
    for i in char:
        if i in password:
            S+=1
    if S == 1 or S == 2:
        cs+=5
    elif S >= 2:
        cs+=10
    return cs , S
cs,S = check_super_symbol(password,char)
coefficient = cl + cr + cn + cs

all_parameters = [lower_count,upper_count,N,S]
if ((lower_count!= 0 or upper_count!= 0) and N != 0 and S!= 0) :
    coefficient+=6
elif not all(all_parameters):
    coefficient+=4

if coefficient<16:
    print("Your password is very easy")
elif coefficient > 15 and coefficient < 25:
    print("Your password is easy")
elif coefficient > 24 and coefficient < 35:
    print("Your password is middle")
elif coefficient > 34 and coefficient < 45:
    print("Your password is strong")
elif coefficient > 44:
    print("Your password is very strong")