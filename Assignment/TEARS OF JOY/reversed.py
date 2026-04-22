"""

reversea string with a loop

"""


word = input("Enter: ")
reversedword = ""
gig = len(word) - 1
while gig >= 0:
    reversedword += word[gig]
    gig -=1
print(f"reversed: {reversedword}")
