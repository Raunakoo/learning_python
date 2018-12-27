#! /anaconda3/bin/python

#circle area = 3.14 * radius ** 2

diameter = int(input("Enter the diameter of the circle that you wnat to find the area and circumfrence"))

radius = diameter/2

area = radius ** 2 * 3.14
circumfrence = radius * 2 * 3.14

print("The radius of your circle is", radius)
print("The diameter of your circle is", diameter)
print("The area of your circle is", area)
print("The circumfrence of your circle is", circumfrence)