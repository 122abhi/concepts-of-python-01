
def number_to_words(n):

    n_dict = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

    ## base Case (When to start combining sub-problems- to get complete solution of the problem)

    if (n // 10 == 0):
        print(n_dict.get(n))
        return

    ## Recursive case
    # Define bigger_problem in terms of smaller sub-problem instances

    extracted_digit = n % 10
    sub_prb = n//10
    number_to_words(sub_prb)
    print(n_dict.get(extracted_digit))

    return

if __name__=='__main__':
    n = 2048
    print('Printing number= {n} in form of words'.format(n=n))
    number_to_words(n)

