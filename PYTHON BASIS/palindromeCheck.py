def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    c = x[::-1]
    print(x,c)

isPalindrome(10)
