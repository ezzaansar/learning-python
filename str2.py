# - Write a program that takes a string as input and returns the number of words in the string.
def count_words(str):
    words = str.split()
    return len(words)
user_input = input("Enter an integer")
words_count = count_words(user_input)
print("the length of string is",words_count)