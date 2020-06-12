'''
Input: a List of integers
Returns: a List of integers

Understand:
takes an array of integers and moves each non-zero integer 
    to the left side of the array, 
    then returns the altered array
doesn't matter what the order of the altered array

Plan:
    use 2 pointers to check for 0 one at each end
    if left pointer sees a zero it swaps with right and 
    if right pointer sees zero, it moves to next index down

'''
def moving_zeroes(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left +=1
            right -=1
        else: 
            if arr[left] != 0:
             left += 1
            if arr[right] == 0:
                right -= 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")