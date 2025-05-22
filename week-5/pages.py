'''
You are given a list of page numbers. Your task is to construct a string that describes the page ranges compactly.
If the list contains all page numbers in the range a...b, this should be presented in the form a–b. 
If the list contains an isolated page number, it should be presented as a single number.
If the list contains multiple page ranges, they should be presented as an ordered list separated by commas. Repeated page numbers should be included only once.
For example, if the list is [3,2,9,4,3,6,9,8], the desired representation is 2-4,6,8-9.
In a file pages.py, implement the function create_string that takes a list of page numbers as a parameter and returns a string of page ranges as described above.
You should implement the function so that it does not modify the input list.
The last test case in the code template prints the list after calling the function and it should be the same as before the call. 
The same requirement applies to all tasks this weeks.
'''

def create_string(pages):
    transformed = sorted(set(pages))

    end = -1
    res = ""
    curr = str(transformed[0])
    itr = 1

    if len(transformed) == 1:
        return curr

    while itr < len(transformed):
        if transformed[itr] - transformed[itr - 1] > 1:
            if end != -1:
                curr += '-' + str(transformed[end]) + ","
                end = -1
            else:
                curr += ","

            res += curr
            curr = str(transformed[itr])


            if itr == len(transformed) - 1:
                res += curr

        else:
            end = itr
            if itr == len(transformed) - 1:
                curr += "-" + str(transformed[end])
                res += curr
        
        itr += 1

    return res





if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]