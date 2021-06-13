
"""
Return nth catalan number.

Formula to get Cn catalan number is:
Cn = (1/n+1) * (2n)Cn
    where, (2n)Cn is nCr as binomial coefficient or combination.

"""

def getCatalan(n):

    Cn = binomialCoefficient(2*n, n)
    Cn = Cn / (n+1)
    return Cn




# Python program to calculate C(n, k)

# Returns value of Binomial Coefficient
# C(n, k)
# https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    if (k > n - k):
        k = n - k
    # initialize result
    res = 1
    # Calculate value of
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)s
    return res


#Driver Code
if __name__ == '__main__':
    n = 5
    returned = getCatalan(n)
    print(returned)

