# LongestWord.py
# Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 
import re


def LongestWord(sen):

    splitted_list = re.split("\W+", sen)
    # code goes here
    return max(splitted_list, key=len)


# keep this function call here
print LongestWord(raw_input())
