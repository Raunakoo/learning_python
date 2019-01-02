x = 1 # x value is 1
i = 5 # i value is 5

while i <= 7: # will keep going while the value of i is less than or equal to 7
    for j in range(1, 5, 2): # range function in for loop will make sequence 1, 3
        x = x * 2 # will run 6 times
    i+=1

print(x) # result will be 64 or 2**6
# note: ** means to the power of