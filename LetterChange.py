# LetterChange.py
# Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 


def LetterChanges(str):
    new_str = list(str)

    for i in range(len(str)):
        str_val = ord(str[i])
        new_str_val = 0
        if 97 <= str_val <= 122:
            new_str_val = str_val + 1
            if new_str_val == 123:
                new_str_val = 97
            new_str[i] = chr(new_str_val)
        else:
            new_str[i] = str[i]

    for i in range(len(new_str)):
        if new_str[i] == 'a':
            new_str[i] = "A"
        elif new_str[i] == 'e':
            new_str[i] = "E"
        elif new_str[i] == 'o':
            new_str[i] = "O"
        elif new_str[i] == 'u':
            new_str[i] = "U"
        elif new_str[i] == "i":
            new_str[i] = "I"
        # code goes here
    return "".join(new_str)


# keep this function call here
print LetterChanges(raw_input())
