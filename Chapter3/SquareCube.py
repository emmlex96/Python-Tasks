"""

PRINT header row (number, square, cube)
FOR number FROM 0 TO 5:
PRINT number, number^2, number^3
(right-aligned)

"""

print("Table of Squares and Cubes")
print(f"{'number':>8}{'square':>8}{'cube':>8}")
for n in range(6):
    print(f"{n:>8}{n**2:>8}{n**3:>8}")
