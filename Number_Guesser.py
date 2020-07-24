import random

guess_num = int(input('Enter any number: '))
end_num = 0
try_num = 1
while end_num != guess_num:
    num_lst = []
    for i in range(len(str(guess_num))):
        num_lst.append(str(random.randint(0,9)))
    gen_num = ''.join(num_lst)
    end_num = int(gen_num)
    print('Try {}: {}'.format(try_num, gen_num))
    try_num += 1
    if end_num == guess_num:
        print('I guessed your number ({}) in {} trys.'.format(end_num, try_num-1))
        break
