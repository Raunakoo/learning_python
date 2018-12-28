name = str(input("type your name "))


space_pos = name.find(" ")

before_space = str(name[0:space_pos])
after_space = str(name[space_pos:])

print("your name reversed is",after_space,before_space)