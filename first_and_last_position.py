def binary_search(lo, hi, condition):
    # We will iterate over the loop until lowest value is small or equal to the highest value
    while lo <= hi:
        mid = (lo + hi) // 2
        # We will pass the mid value to the condition to check where is our target value in the list
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        else:
            lo = mid + 1

    return -1

# Let's write a function to return the first occurrance of the target
def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid ] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums)-1, condition)

# Let's write a function to return the last occurrance of the target
def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums)-1, condition)

# Now let's write the final function to return first and last position of the target
def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


print(first_and_last_position([1,1,2,3,4,5,6,6,6,6,6,7, 9, 10], 11))



