def find_word(word_list):
    max_length = "" 
    for i in word_list:
        if "a" in i:
            if len(max_length) < len(i):
                max_length = i
    if max_length:
        print(max_length)
    else:
        print("not found")