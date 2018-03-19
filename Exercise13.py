def fibonacciList(num):
    '''
    Creates a list of fibonacci numbers based on the size of the users number
    '''
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

    
userNumber = int(input("Please select the number of fibonacci numbers"))
print(fibonacciList(userNumber))

