import sys 

# Set up a list for our code to work with that omits the first CLI argument, 
# which is the name of our script (fizzbuzz.py)
inputs = sys.argv
inputs.pop(0)

# Now, inputs is ready for us to work with
for num in inputs:
    if (int(num) % 15 == 0):
        print("fizzbuzz")
    elif (int(num) % 5 == 0):
        print("buzz")
    elif (int(num) % 3 == 0):
        print("fizz")
    else:
        print(int(num))
