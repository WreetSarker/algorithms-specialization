def linearSearch(lst, query):
    # Set the position to be 0
    position = 0

    # Set up a loop for execution
    while position < len(lst):

        # Check if the index position of the list matches the query
        if lst[position] == query:

            # Done! Result found... Return the position
            return position

        # Increment the postion by 1
        position += 1


    # We didn't find the query... Return -1
    return -1


print(linearSearch([1,4,2,5,6,8,8,0,9], 21))
