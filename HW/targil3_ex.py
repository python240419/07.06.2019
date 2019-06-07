
targil = input("Enter 1st number: ") # 3 + 4 = 7
list = targil.split() # [3, +, 4, =, 7]
a = int(list[0])  # 3
oper = list[1]    # +
b = int(list[2])  # 4
c = int(list[-1]) # 7
result = False

# if a + b == c:
#   result = True
# else:
#     result = False
# shortcut: result = a + b == c

if oper == "+":
    result = a + b == c
elif oper == "-":
    result = a - b == c
elif oper == "*":
    result = a * b == c
elif oper == "/":
    result = a / b == c
elif oper == "//":
    result = a // b == c
else:
    print(f'{oper} is an unknown sign!')

if result == True:
    print("Correct!")
else:
    print("wrong!")
