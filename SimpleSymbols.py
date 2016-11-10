# SimpleSymbols.py
# Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 


def SimpleSymbols(str):
    _str = str.lower()
    for i in range(len(_str)):
        if _str[i].isalpha():
            if i == 0 or i == len(_str):
                return 'false'
            if _str[i - 1] != '+' or _str[i + 1] != '+':
                return 'false'
    # code goes here
    return 'true'

# keep this function call here
print SimpleSymbols(raw_input())
