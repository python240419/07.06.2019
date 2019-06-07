
targil = input("Enter 1st number: ") # 3 + 4 = 7
list = targil.split() # [3, +, 4, =, 7]
a = int(list[0])  # 3
oper = list[1]    # +
b = int(list[2])  # 4
c = int(list[-1]) # 7

if oper == "+":
    if a + b == c:
        print("Correct!")
    else:
        print("wrong!")
elif oper == "-":
    if a - b == c:
        print("Correct!")
    else:
        print("wrong!")
elif oper == "*":
    if a * b == c:
        print("Correct!")
    else:
        print("wrong!")
elif oper == "/":
    if a / b == c:
        print("Correct!")
    else:
        print("wrong!")
elif oper == "//":
    if a // b == c:
        print("Correct!")
    else:
        print("wrong!")
else:
    print(f'{oper} is an unknown sign!')
