# calculate sum of table
table= [[1,2],[3,4]]
sum1 = 0
for row in range(len(table)):
    for column in range(len(table[row])):
        sum1 = sum1 + table[row][column]

print(sum1)
