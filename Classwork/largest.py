def largest_number(first_number, second_number, third_number):
    largest = first_number
    if second_number > first_number:
        largest = second_number
    if third_number > second_number:
        largest = third_number
        
        return largest
print(largest_number(80,90,100))
