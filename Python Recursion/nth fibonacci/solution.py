# given an integer n
# compute nth term of the fibonacci series

# eg: if n=5
# then fibonacci series= 0,1,1,2,3,5 (5th term)
# fibonacci term = sum of previous two fibonacci terms

# A fibonacci term can be explained in terms of other fibonacci terms ( here, sub-problems)
# Therefore, clearly this problem can be explained into smaller sub-problems
# Thus we go for recursion solution

def sol_fibonacci(n):
    # if n is 5 then compute fibonacci series and return 5th term
    # bottom-up approach
    # if n is 5 then compute fibonacci series and return 5th term
    # top-down approach

    ## base case (when to start combining sub-problems - to get complete problem solution
    if (n == 0):
        return 0
    elif (n==1):
        return 1

    ## Recursion case
    # Define bigger_problem in terms of smaller sub-problem instances

    bigger_prb_n = sol_fibonacci(n-1) + sol_fibonacci(n-2)
    return bigger_prb_n

if __name__=="__main__":
    result = sol_fibonacci(3)
    print(result)




