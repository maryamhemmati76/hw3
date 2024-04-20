def find_vowels(text):
    vowels = 'aeiou'
    my_dict = {}

    for i in vowels:
        my_dict[i] = 0

    text_lower = text.lower()
    for i in text_lower:
        if i in vowels:
            my_dict[i] += 1

    return my_dict

text =input("enter your text: ")
result_dict = find_vowels(text)
print(result_dict)