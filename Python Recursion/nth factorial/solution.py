# Given a n integer number
# Print nth factorial

# clearly this problem can be explained into small sub-problems
# Thus we go for recursion solution

# let's divide/break solution as n = n * (n-1)..

def sol_fact(n):

    ## Base Case: when to start combining sub-problems- to get complete problem solution

    if (n==0):
        return 1

    ## Recursion case
    # Define bigger problem in terms of smaller problem instances
    #bigger_problem = n * smaller_problem
    bigger_problem = n * sol_fact(n-1)
    return bigger_problem

if __name__=="__main__":

    result = sol_fact(5)
    print(result)



