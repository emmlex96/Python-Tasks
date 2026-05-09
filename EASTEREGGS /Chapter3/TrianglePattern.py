"""
increasing left-aligned triangle

FOR row FROM 1 TO 10:
FOR col FROM 1 TO row:
PRINT '*' (no newline)
PRINT newline

decreasing left-aligned triangle
FOR row FROM 10 TO 1:
FOR col FROM 1 TO row:
PRINT '*' (no newline)
PRINT newline

"""


print("Pattern (b):")
for row in range(10, 0, -1):
    for _ in range(row):
        print('*', end='')
    print()
