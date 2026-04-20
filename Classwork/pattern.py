"""
display the patterns of numbers

54321
4321
321
21
1
"""

for number in range(5,0,-1):
    for count in range(number, 0, -1):
        print(count, end=" ")
    print()
