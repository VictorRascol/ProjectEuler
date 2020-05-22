limit = 4000000
firstNum = 1
secondNum = 2
totalSum = 0

while secondNum < limit:
    if (secondNum % 2 == 0):
        print(secondNum)
        totalSum = totalSum + secondNum
    newNum = 0
    newNum = firstNum + secondNum
    firstNum = secondNum
    secondNum = newNum
print(totalSum)