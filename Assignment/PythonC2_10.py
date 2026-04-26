numberone = int(input("enter number: "))
numbertwo = int(input("enter number: "))
numberthree = int(input("enter number: "))

sum = numberone + numbertwo + numberthree
average = sum / 3
product = numberone * numbertwo * numberthree

print(sum)
print(average)
print(product) 

largest = numberone
if numbertwo > largest:
   largest = numbertwo
if numberthree > largest:
   largest = numberthree
print(largest)

smallest = numberone
if numbertwo < smallest:
    smallest = numbertwo
if numberthree < smallest:
    smallest = numberthree
print(smallest)

