def checkPrime(userNum):
    '''
    Checks if the users entered number is a prime number or not
    '''
    oneToNum = []#Creates a list starting from 1 - userNum
    divisorList = []#Empty list to be filled with divisors form userNum

    i = 1

    while i <= userNum:
        oneToNum.append(i)
        i += 1
    
    for number in oneToNum:
        if userNum % number == 0:
            divisorList.append(number)

    #Check if list is prime
    if divisorList[0] == 1 and divisorList[1] == userNum:
        print("Number is prime")
    else:
            print("Number is composite")
    

userNum = int(input("Please choose a number to check for primality:"))
checkPrime(userNum)
