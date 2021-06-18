

def isPrime(n: int)->bool:
    """
    Give an Integer 'n'. Check if 'n' is Prime or Not
    :param n:
    :return: bool - True or False

    We will use Naive approach.
    Check Divisibility of n with all numbers smaller than n.
    If any one of the smaller number is able to divide n, then n is instantly identified as not Prime & we return False.
    Else, If none of the smaller numbers in range 2 to n-1 range, were able to divide n then N is surely Prime & we return True.
    """
    #Explicitly check if n is '1'
    if (n == 1):
        return False

    #check divisibility of n -by any number in range 2 to n-1.
    # a number i.e other than 1 & itself within

    i=2
    while(i<n):
        if n% i == 0:
            #it is divisible by i therefore
            return False
        i = i+1
    # n is not divisible by any no. in range 2 to n-1.
    return True

#Driver Code
if __name__ == '__main__':

    n = 24971
    returned = isPrime(n)
    print(returned)
