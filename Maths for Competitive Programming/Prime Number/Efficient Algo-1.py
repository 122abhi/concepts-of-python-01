

def isPrime(n: int)->bool:
    """
    Give an Integer 'n'. Check if 'n' is Prime or Not
    :param n:
    :return: bool - True or False
    A no. is prime if it is divisible only by 1 & itself.
    1- is neither Prime nor Composite

    We will use Naive approach.
.   Check Divisibity of n with all numbers smaller than n. within range 2 to sqrt(n).

All divisors of n comes as pairs. Thus if n is not divisible by any no. within range 2 to sqrt(n), then it is Prime.
WE reduce range from 2 to n to 2 to sqrt(n)
    """
    if n==1 :
        return False
    i = 2
    while (i * i <= n ):
        if ( n % i ==0):
            return False
        i = i+1
    return True


#Driver Code
if __name__ == '__main__':

    n = 24971
    returned = isPrime(n)
    print(returned)
