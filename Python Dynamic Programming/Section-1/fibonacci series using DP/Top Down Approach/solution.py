
# Dynamic Programming
# Optimal sub-structure: Sub-problems are there
# over-lapping sub0problems: more than 1 sub-problems are over-lapping

# Top- Down approach : Adding memoization to you recursion solution

# in Top-down approach we start from bigger problem and build the solution recursively
# while combining individual solutions of the sub-problems

# In Simple term: We add a memory component in our recursive solution. (data structure like, array,etc)


def sol_fibonacci_dp(n, dp: list):

    ## Base Case: When to start combining smaller sub-problems - to get complete problem's solution

    if ((n == 0) or (n==1)):
        return n

    ## Recursive solution

    ## Add lookup code before computing a recursive value
    if dp[n] is not None:
        return dp[n]

    # Add passing of DP data structure as argument to the function.
    bigger_prb = sol_fibonacci_dp(n-1, dp) + sol_fibonacci_dp(n-2, dp)

    ## Store recursive value(bigger_prb) before returning it to the stack
    dp[n]=bigger_prb
    return bigger_prb

if __name__=="__main__":
    """Dirver Code"""

    n = 10
    dp = [None] * 100

    result= sol_fibonacci_dp(n, dp)
    print("{n}th fibonacci number using DP is: ".format(n=n), result)
    print("At end the DP memoization data structure value is: ", dp)