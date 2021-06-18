

def isPrime(n: int)->bool:
    """
    Give an Integer 'n'. Check if 'n' is Prime or Not
    :param n:
    :return: bool - True or False
    A no. is prime if it is divisible only by 1 & itself.
    1- is neither Prime nor Composite

    - check for n being a even number i.e divisble by 2
    - check for n being divisible by 3
    - then create a range of i following series, 5,7,11,13,17,19,23,.... till sqrt(n) with step as +6
    - check for divisibility of n with each value of i & i+2
    """
    if n== 1:
        return False
    # handle boundary conditions
    if n == 2 or n==3:
        return True
    # Now check for divisibility of n by 2 & 3
    if n % 2 ==0 or n % 3 ==0:
        return False

    i = 5
    while (i*i <= n):
        if n%i ==0 or n%(i+2) ==0:
            return False

        i = i+ 6
    return True


#Driver Code
if __name__ == '__main__':

    n = 24971
    returned = isPrime(n)
    print(returned)
