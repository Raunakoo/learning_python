count = 0
for i in range(2):
    word = input("word ")
    position = word.find("w")

    if position != -1:
        count += 1

        word = word[position:]
    if word.find("w") != -1:
        count +=1
    
    if count == 2:
        print(word)

    else:
        print("your entered word doesn't contain two W")
        continue