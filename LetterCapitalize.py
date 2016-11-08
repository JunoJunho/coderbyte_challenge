# LetterCapitalize
# Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space. 
import re


def LetterCapitalize(str): 
    re_str = re.split("\W+", str)
    for i in range(len(re_str)):
        re_str[i] = re_str[i][0].capitalize() + re_str[i][1:]
    # code goes here 
    return " ".join(re_str)
    
# keep this function call here  
print LetterCapitalize(raw_input())