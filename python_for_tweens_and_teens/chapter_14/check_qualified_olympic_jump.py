import math

jumpA = int(input("First Jump "))
jumpB = int(input("Second Jump "))
jumpC = int(input("Third Jump "))

average_jump = (jumpA + jumpB + jumpC)/3

if average_jump > 8:
    print("Qualified")
else:
    print("Unqualified")

print("Olympics")