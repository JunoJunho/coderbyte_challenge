# CheckNums.py
# Using the Python language, have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1. 

def CheckNums(num1,num2):

    if int(num1) > int(num2):
        return 'true'
    elif int(num1) < int(num2):
        return 'false'
    else:
        return '-1'
    
# keep this function call here  
print CheckNums(raw_input())