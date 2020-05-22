multiple1 = 3
multiple2 = 5
limit = 1000
totalSum = 0

for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
        totalSum = totalSum + i

print(totalSum)
    