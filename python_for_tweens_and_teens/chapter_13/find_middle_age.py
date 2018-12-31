first_age = input("first age ")
second_age = input("second age ")
third_age = input("third age ")

list = [first_age, second_age, third_age]

#sort method puts list in order
list.sort(reverse = True)

print("the list from greatest ot least is,", list)
print("the middle age is", list[1])