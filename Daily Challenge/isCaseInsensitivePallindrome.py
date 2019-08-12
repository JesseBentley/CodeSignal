def isCaseInsensitivePalindrome(inputString):
    input_string = inputString.casefold()
    reversed_string = reversed(input_string)
    if list(reversed_string) == list(input_string):
        return True
    else:
        return False