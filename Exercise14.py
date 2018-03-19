def removeDuplicatesLoop(dupList):
    '''
    This function creates a new list omitting duplicates via the use of a 
    loop and condition statement
    '''
    newList = []
    
    for element in dupList:
        if element not in newList:
            newList.append(element)
    
    return newList

def removeDuplicatesSets(dupList):
    '''
    This function uses the integrated funtion of sets.
    In Mathematics, a set is a collection of distinct objects
    '''
    return set(dupList)

dupList = [1,1,2,56,78,54,54,54,54]
print(removeDuplicatesLoop(dupList))
print(removeDuplicatesSets(dupList))
