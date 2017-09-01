def fibonacci(x):
    ''' This function generates the first x values of the Fibonacci sequence as a list.'''
    if (x < 3):
        fibseq = [1] * x
    else:
        fibseq = [1] * 2
        for i in range(2, x):
            fibseq.append(fibseq[i - 2] + fibseq[i - 1])
    return fibseq