# Give an array arr of length n
# recursively check if the given array is sorted ascendingly?

# is array sorted?
# we can check sorting state of an array by checking
# sorting state of it's sub-sequent smaller array

# i.e let's divide N array into 1 + (n-1) length of array.
#   (we can also divide into two arrays, each of length N/2)

# Therefore, Clearly we can break/divide this problem into same smaller
# sub-problem instances

def is_sorted_asc(arr):

    ## base case (when to start combining sub-problems - to get complete problem solution
    # n ==1 i.e when smaller_problem will be only 1 digit array: we will want to return True
    # as 1 element array is always sorted

    # Also n==0 for the case if the initial array itself is of zero length.
    if ((len(arr) == 1) or (len(arr) == 0)):
        return True

    ## Recursive case: Define bigger problem in terms of smaller sub-problem instances

    bigger_prb = is_sorted_asc(arr[1:])

    if (bigger_prb == False):
        return False
    if arr[0]< arr[1]:
        return True
    else:
        return False

# ## Whenever, you feel getting nested if conditions u can combine them using logical operators
#     if arr[0]< arr[1] and is_sorted_asc(arr[1:]):
#         return True
#     else:
#         return False

if __name__=="__main__":
    ## Driver Code

    sorted_list = [1,2,3,4,5]

    result = is_sorted_asc(sorted_list)
    print(sorted_list, "is sorted?")
    print(result)

    un_sorted_list = [1,2,3,5,4]

    result = is_sorted_asc(un_sorted_list)
    print(un_sorted_list, "is sorted?")
    print(result)




