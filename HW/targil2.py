
a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

if a > b and a > c:
    # a is the biggest
    print(f'{a} is biggest (equal)')
elif b > c:
    print(f'{b} is biggest (equal)')
else:
    print(f'{c} is biggest (equal)')

