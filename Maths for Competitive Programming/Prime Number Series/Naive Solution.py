

def printPrimes(n: int):
    """
Problem Statement:
    - Given an Integer 'n'
    - Print all Prime numbers that are smaller than or equal to 'n'

Solution approach:
    We will use Naive approach.
    -Run loop i= within 2 to n+1
    - if i is isPrime(i)
    - print i

    :param n:
    :return:
    """

    i = 2
    while(i<=n):
        if (isPrime(i) == True):
            print(i)
        i = i + 1

#Driver Code
if __name__ == '__main__':

    n = 24971
    #printPrimes() uses isPrime() function.

    def isPrime(n: int) -> bool:
        """
        Give an Integer 'n'. Check if 'n' is Prime or Not
        :param n:
        :return: bool - True or False
        A no. is prime if it is divisible only by 1 & itself.
        1- is neither Prime nor Composite

        """
        if n == 1:
            return False
        # handle boundary conditions
        if n == 2 or n == 3:
            return True
        # Now check for divisibility of n by 2 & 3
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while (i * i <= n):
            if n % i == 0 or n % (i + 2) == 0:
                return False

            i = i + 6
        return True
    #printPrimes() uses isPrime() function.
    printPrimes(n)


