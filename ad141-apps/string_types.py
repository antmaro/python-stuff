#!/usr/bin/env python3

print("AbCDe".isalpha(), "AbCD123".isalpha())
print("123".isnumeric(), "12.3".isnumeric())
print(" \t\n".isspace(), "a b\t\n".isspace())
print("ABCD".isupper(), "abcd".isupper())

# more strings

word = "is"
sentence = "The capital of Mississippi is Jackson."
position = sentence.find(word)
print("First: ", position, "\t2nd: ", sentence.find(word, position + 1))
print(sentence.find(word, 8,19))
print("the word '", word, "' appears", sentence.count(word), "times.\n")
print("Right Justified:", word.rjust(15), "|")
print(" Left Justified:", word.ljust(15,"*"), "|")
data = "1 4 1 1abc"