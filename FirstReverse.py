# FirstReverse.py
# Using the Python language, have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

def FirstReverse(str): 

    # code goes here 
    ret_str = ""
    for i in range(len(str)-1, -1, -1):
    	ret_str += str[i]
    return ret_str
    
# keep this function call here  
print FirstReverse(raw_input())  