def firstAndLastList(a):
    '''
    Takes list as an argument and returns a new list
    consisting of the first and last elements,resepecitivly 
    '''
    newList = []
    
    newList.append(a[0])
    newList.append(a[-1])
    
    return newList

    

a = [5, 10, 15, 20, 25]
print(firstAndLastList(a))
