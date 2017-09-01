def fibonacci(x):
    ''' This function generates the first x values of the Fibonacci sequence as a list.'''
    if (x < 3):
        # first two numbers in sequence are 1
        fibseq = [1] * x
    else:
        # begin with first two 1's in sequence
        fibseq = [1] * 2
        # iterate for i from 2 to x
        for i in range(2, x):
            # append sequence
            fibseq.append(fibseq[i - 2] + fibseq[i - 1])
    # return value
    return fibseq