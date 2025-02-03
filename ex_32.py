the_count = [1,2,3,4,5]
fruits =['apples','watermelon','oranges','pears']
bikes = [1, 'ktm',2,'r15',3,'royal enfield']

#first kind of for loop through the list

for number in the_count :
    print(f"this is count {number}")
#same as above

for fruit in fruits :
    print(f"A fruit of type :{fruit}")

# now going through mixed  list

for i in bikes:
    print(f"i got {i} ")

#building list,starting with an empty one
elements = []

#using range of unction to do 0 to 5 counts
for i in range(0,6):
    print(f"adding {i} ot the list.")
    #append is a function that list understand
    elements.append(i)

#printing out
for i in elements:
    print(f"elements was : {i}")

    