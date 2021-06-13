


# Declare lookup table
# initialize base values of i's
# next we run loop that iterating over remaining values of 'i'
#
# then we fill the table for remaining values of i by running a for loop for range of remaining value of i to of nth value
# for each iteration- we calculate & update result of i as a combination of previous i's.

# Finally we return the required value as return table[n]

def getCatalan(n):

    # Declare lookup table - such that it can save result for nth, if n=5 then n+1=6 i.e list of 6 length.
    # it will have 0,1,2,3,4,5 indexes
    table: list = [0] * (n+1)
    # We here are Initializing a sum=0 for ith value too.
    # initialize base values
    table[0] = table[1]= 1

    for i in range(2, n+1):
        # calculate values for remaining i values
        # here, we have summation formula therefore, 1 more for loop
        Cn=0
        for j in range(0, i):

            Cn += table[j] * table[(i-1)-j]

            #table[i]+= table[j] * table[(i-1)-j]
            # If we dono't want to use Cn as intermediate variable
        table[i] = Cn
        # updating the lookup table with result of ith value

    # returning needed value as table[n], nth index.
    return table[n]



#Driver Code
if __name__ == '__main__':
    n = 5
    returned = getCatalan(n)
    print(returned)









