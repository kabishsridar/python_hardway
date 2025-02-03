i = 0
numbers = []
#now assigning while statement
while i <6:    
    print(f"at the top is {i}")
    numbers.append(i)
#now appending numbers
#the num.append adds a single item to existing lists
    i = i +1
    print("numbers now ", numbers)
    print(f"at the bottom i is {i}")

print("the numbers :")

for num in numbers:    
    print(num)

    