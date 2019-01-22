'''
This code creates two lists a and b, 
and then chooses the greatest number on 
each position from both and creates a new list.
################################################
The code has the following steps:
1. Create a variable called numbers 
   and give it a value of 20
2. Create two empty datatypes, a and b
3. Ask user input for number, 
   as to create lists a and b
4. Create an empty datatype(array)
5. Create a loop, for j in range(numbers)
6. Use if and else statements to check,
   if at a given position, the value 
   in array a or b is greater
'''
print("This code creates two lists a and b" + 
    "and then chooses the greatest number on" +
    "each position from both and creates a new list.")

# 20 numbers
numbers = 4

#a and b lists
a = [None] * numbers
b = [None] * numbers

#ask user in range of numbers
for i in range(numbers): 
    a[i] = int(input("Type a number for list a ")) 
for i in range(numbers): 
    b[i] = int(input("Type a number for list b "))

array = [None] * numbers
for j in range(numbers):
    if a[j] > b[j]:
        array[j] = a[j]
    else:
        array[j] = b[j]

print("Your array is",array)