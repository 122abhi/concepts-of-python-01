
"""
Return nth catalan number.

Recursive Formula of Catalan Numbers says:
C of (n+1) = summation of C of i* C of n-i, for range i=0 to i=n
Therefore, for C of n formula becomes

C of (n) = summation of C of i* C of n-1-i, for range i=0 to i=n-1

"""

def getCatalan(n,dp_arr):
    # Lookup
    if (dp_arr[n] is not None):
        return dp_arr[n]

    #Base Case
    if (n==0):
        return 1

    #Rec Case
    Cn = 0
    for i in range(0,n):
        Cn = Cn + ( getCatalan(i, dp_arr) * getCatalan(n-1-i, dp_arr) )

    dp_arr[n] = Cn

    return Cn

#Driver Code
if __name__ == '__main__':
    dp_arr : list = [None] * 100
    n = 5
    returned = getCatalan(n, dp_arr)
    print(returned)
