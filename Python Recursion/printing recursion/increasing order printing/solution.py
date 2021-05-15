# Given an Integer n
# Print first n numbers in increasing order (do not print 0)
# using recursion

# eg: n = 5
# print: 1, 2, 3, 4, 5

# using recursion solving this

# we will try to go till the base case & then
# build the solution i.e print while combining the sub-problems

def sol_print(n):
    ## base case: condition on which to start combining sub-problems- to get complete problem's solution.
    if (n ==1):
        print(n)
        return

    ## recursion case: define bigger_problem in terms on smaller_problem
    # when n was 2
    # here sol_print(1) wil be called
    # when sol_print(1) is called it will go into base case, it will print 1 and return
    # it will return at sol_print(2) 24th line & then will move to 25th line of sol_print(2)
    sol_print(n-1)
    print(n)
    return

## print statement written after recursive call is bottom-up appraoch
## print statement written before recursive call is top-down approach

# you can replace print statemnts with some other code the direction of flow will remain same.

if __name__=="__main__":
    result = sol_print(5)
    print("Increasing Program completed")
    print("Solved recursively")
