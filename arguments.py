print(1,2,3,4,5)

number =  [1,2,3,4,5]
print(number)

print(*number)

print((1,2,3,4,5))

print(*"abc")

def add(*num):
    total = 0
    for numb in num:
        total = total+numb
    return total     

print(add(4,5,4555,34546,3345)) z