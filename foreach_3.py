
numbersList = [[1, 300, 5], [7, 800, 9], [-4, 100000, 200]]

print(numbersList)

# for inside for
for currentList in numbersList:
    print(currentList)
    sum = 0
    for number in currentList:
        sum = sum + number
        print(number, sum)
        if sum > 100:
            break
    print("after list....")

