import random

# Get the user input
user_guess = int(input('Enter any number: '))

# Instantiate global variables
guess_lst = []
try_count = 1

# Length of user input
ug_length = len(str(user_guess))

# Infinite loop for guessing
while True:
    # Empty list for adding random integer with length ug_length
    num_lst = []
    
    # If user input is > a digit, then the first number of my guess is != 0
    if ug_length > 1:
        num_lst.append(str(random.randint(1,9)))
    else:
        num_lst.append(str(random.randint(0,9)))
    
    # Add random integers to num_lst to match ug_length
    for i in range(ug_length-1):
        num_lst.append(str(random.randint(0, 9)))
    
    # Join all the numbers in num_lst and convert to int
    new_num = int(''.join(num_lst))
    
    # Add new_num to guess_lst if not already guessed, else restart iteration
    if new_num not in guess_lst:
        guess_lst.append(new_num)
        print('Try {}: {}'.format(try_count, new_num))
        try_count += 1
    else:
        continue
    
    # If the new_num is user input, print # of tries and break
    if new_num == user_guess:
        print('I guessed your number in {} tries'.format(try_count))
        break
