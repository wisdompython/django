#fibonacci sequence generator

# sequence usually starts with  a 0  and 1
first_num = 0
second_num = 1

# get user input on how long the fibonacci sequence should run.
len_Sequence = int(input('To what nterm would you love this sequence to run'))

# if user inputs 1 only print the first integer in the series
if len_Sequence ==1:
    print(first_num)
else:
    print(first_num)
    print(second_num)
    for i in range(2, len_Sequence):
        added_num = first_num + second_num
        first_num = second_num
        second_num = added_num
        print(added_num)
