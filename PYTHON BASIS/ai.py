import random
def write_random_array_of_length_5(arr): 
    arr = [random.randint(1, 10) for i in range(5)]
    print([x for x in arr])

print(write_random_array_of_length_5([]))