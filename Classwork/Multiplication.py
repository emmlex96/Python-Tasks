"""
a 7 multiplication table from 1 to 10
"""
table = int(input(" Enter times table number"))
for count in range(1,11):
    print(table,"X", count, " = ", table * count)
