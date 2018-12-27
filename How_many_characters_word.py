word_to_count_character = input("enter a word ")

# Len function counts the number of characters in a string
print(len(word_to_count_character))

word_list = list(word_to_count_character)
# reverse the string
word_reversed = ("".join(list(reversed(word_list))))

if word_reversed == word_to_count_character:
    print("Your word,", word_to_count_character,",is a palindrome")

else:
    print("your word,",word_to_count_character,",is not a palindrome")