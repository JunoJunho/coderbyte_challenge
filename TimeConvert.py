# TimeConver.pt
# Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 

def TimeConvert(num):
    int_num = int(num)
    hour = int_num / 60
    minuts = int_num % 60
    # code goes here
    return str(hour) + ":" + str(minuts)


# keep this function call here
print TimeConvert(raw_input())
