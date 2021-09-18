def binarySearch(lst, query):
    # First set the low and high points
    lo, hi = 0, len(lst)-1

    # Create a loop to iterate over the list
    while lo <= hi:
        # Create a middle point of the list
        mid = (lo + hi)// 2
        mid_num = lst[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_num)

        # Check to see if the mid number is equal to the query or not
        if mid_num == query:
            return mid

         # If the query is less than the mid number than set the hi to 1 before the mid   
        elif query < mid_num:
            hi = mid - 1

        # Otherwise set the lo to 1 plus the previous mid   
        else:
            lo = mid + 1

    # If the query is not found, return -1
    return -1


print(binarySearch([1,4,15,19,31,33,55,66,77,88,99,123,145,161,171,181], 88))

