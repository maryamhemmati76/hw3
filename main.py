from src.hw3_1 import find_word
from src.hw3_2 import palindrome
from src.hw3_3 import find_vowels

word_list = ["banana", "apple", "cherry", "grape", "kiwi", "date"]
find_word(word_list)

word_list = ["new york", "toronto", "london", "greece"]
find_word(word_list)

txt="A man, a plan, a canal, Panama"
palindrome(txt)

txt="Hello, World!"
palindrome(txt)

text =input("enter your text: ")
result_dict = find_vowels(text)
print(result_dict)