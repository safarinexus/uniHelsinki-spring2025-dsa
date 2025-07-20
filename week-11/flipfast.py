'''
An earlier task this week was to efficiently simulate steps, where the first two elements of a list are moved to the end of the list in reverse order.
The task can be solved even more efficiently in a way that does not simulate each step separately.
In a file flipfast.py, implement the function find_first that takes the list size and the number of steps as parameters.
The function should return the first element of the list after the steps.
The function should return an answer quickly even with very large parameters.
The last function call in the code template tests this situation.
'''

import collections

def find_first(size, steps):
    current_list = collections.deque(range(1, size + 1))

    # Perform the reordering steps
    for _ in range(steps):
        # Check if there are at least two elements to move
        if len(current_list) < 2:
            # If fewer than 2 elements, the process stops effectively
            # as you can't take the "first two elements".
            # The problem implies n >= 2 for steps to occur,
            # and num_steps can be less than n-1.
            break 
            
        # 1. Get the first two elements
        first_element = current_list.popleft()
        second_element = current_list.popleft()

        # 2. Move them to the end in reverse order
        current_list.append(second_element)
        current_list.append(first_element)

    # The first element of the list when all steps have been completed
    # If the list becomes empty (e.g., n=0, though validated), this would error.
    # Given n >= 1, the list will never be empty.
    return current_list[0]

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959