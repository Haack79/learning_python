import sys

def hail_friend(friend):
    print(f"Hail, {friend}!")

def add_numbers(first_number, second_number):
    result_sum = first_number + second_number
    return result_sum
    # To complete this challenge, 
    # you will need to compare the values of the numbers passed in to your script as 
    # arguments. However, when you initially read them from sys.argv, 
    # those values will be strings and not numbers. To do numeric comparisons on them,
    #  we will need to convert the arguments to integers (whole numbers) or floats (decimal numbers). 
    # The code below shows how to convert inputs to integers.
    # first_num = int(sys.argv[1])
    # second_num = int(sys.argv[2])
    # sum_to_use = first_num + second_num
