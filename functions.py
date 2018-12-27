'''def add(x,y):
    return x + y


x = add(5,6)

print(x)

def rev(text):
    print(text[::-1])

rev("John")'''

def info(name,age,likes):
    detail = "I am {}. I am year old {} and I like {}".format(name,age,likes)

    return detail


dictionary = {"name" : "john", "age" : str(34), "likes" : "ptyhon"}

print(info(**dictionary))

import math
     
def main():
    math.cos(math.pi)
main()
print(main())

def about(**kwargs):
    for key, value in kwargs.items():
        print("{} - {}".format(key,value))

about(python = "easy", Java = "hard")

f = [ (a,b) for a in range(0,3) for b in range(a) ]

print(f)

for a in range(0,3):
    print(a)
    for b in range(a):
        print("this is b",b)
        print("this is a ",a)

print (type(type(int)))

print(0.1+0.2)