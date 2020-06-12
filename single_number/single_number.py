'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

Understand:
    when a number is not a pair it should be returned.
    
    valid or invalid inputs
        invalid: letters
        valid: integers

Plan:
    count the times each appears
    if the counter is not 2 at the end, return it
    or
    if value[i] = value[i+1] and counter is at 2
    increase pointers by one
    elif i != i+1 and counter is not 2, return value[i]



'''
def single_number(arr):
    
    shows = 0 # the number of times a value appears

    for i in range(len(arr)):
        #if the value


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")