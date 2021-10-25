import random
a = ["Once upon a time ", "Yesterday ", "Sometime in the future "]
b = ["a man ate a bean ", "someone cooked salmon ", "a disabled elderly cooked a pie "]
c = ["And it was tasty.", "And it was awful.", "And it needed salt."]

def storyMaker():
    d = a[random.randint(0,2)] + b[random.randint(0,2)] + c[random.randint(0,2)]
    return d
storyMaker()