"""
Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example

"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
"""

def isPalindrome(str):
 
    symbols = []

    for item in range(len(str)):
        if (str[item] in symbols):
            symbols.remove(str[item])
        else:
            symbols.append(str[item])

    if (len(symbols) == 0 or len(symbols) == 1):
        return True
    else:
        return False


print(isPalindrome("abcab"))
