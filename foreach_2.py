
numbers = [4, 9, -5, 70, 84, 1830, 20, 30, 600, 1000, 200, 300]

sum = 0

for number in numbers:
    sum = sum + number
    print(f'{number} current sum = {sum}')
    if sum > 100:
        break

for number in numbers [2:-1]:
    sum = sum + number
    print(f'{number} current sum = {sum}')
    if sum > 100:
        break

