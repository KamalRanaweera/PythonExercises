# Lists
# A list can hold multiple values

# Defining a list called numbers with no values in it
numbers = []
print(numbers)

numbers.append(10)
print(numbers)

numbers.append(15)
print(numbers)

numbers.append(-15)
print(numbers)

# Initialize a list while creating it
myList = [2, 5, -4, 25, 100]
print("myList =",myList)

# Printing the values of myList in one value per line
print("Printing elements one by one")
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])

# We can use a FOR loop to print these values easily
print("Using a FOR loop")
for val in myList:
    print(val)

# Let's uses a FOR loop to add all values in myList
total = 0
for val in myList:
    total = total + val
    print("Current total =", total)

print("Final total = ", total)

# If we need to use a FOR loop to iterate through a 
# range of number from 1 to 100, we can use the "range"
# function instead of defining a list from 1 to 100.

# Add all number from 1 to 100 using a FOR loop
total = 0
for i in range(1, 100):
    total = total + i

print("Sum of numbers from 1 to 100 =", total)

# List with strings
fruits = ["Banana", "Apple", "Grape", "Pineapple"]
for fruit in fruits:
    print(fruit)


