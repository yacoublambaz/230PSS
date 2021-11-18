"""

Problem 1)

Given a list L, which contains strings L = ["hello","wassup","this","is","yacoub"]
and a strIn hellothis, return the indices of the two strings in L that
add up to strIn

Problem 1.a) asked you to do this in O(n^2)

"""

def strSearchV1(L,inStr):
    for i in range(len(L)):
        for j in range(i,len(L)):
            if L[i] + L[j] == inStr:
                return (i,j)
    return (-1,-1)

"""

Problem 1.b) asked us to do it in O(nlogn)

"""

def strSearchV2(L,inStr):
    """
    1) sort L
    2) for loop over L to get L[i]
    3) I extract the L[j] such that L[i] + L[j] == inStr
    4) to find L[j], I implement binarySearch on the sorted list
    5) which got me the index of L[j] in the sorted list, I need to find it
    in the not sorted list
    6) if I didn't find it, just return (-1,-1)
    """
    def binarySearch(sortedL,strNeeded,low,high):
        if low>high:
            return -1
        mid = (low+high)//2
        if sortedL[mid] == strNeeded:
            return mid
        if sortedL[mid] > strNeeded:
            return binarySearch(sortedL,strNeeded,low,mid-1)
        else:
            return binarySearch(sortedL,strNeeded,mid+1,high)
    sortedL = sorted(L)
    for i in range(len(L)):
        strNeeded = inStr[len(L[i]):]
        indexOfStrNeededInSortedList = binarySearch(sortedL,strNeeded, 0, len(sortedL)-1)
        indexOfStr1InOriginalList = i
        if indexOfStrNeededInSortedList != -1:
            break
    if indexOfStrNeededInSortedList == -1:
        return (-1,-1)
    for i in range(len(L)):
        if L[i] == sortedL[indexOfStrNeededInSortedList]:
            indexAns = (indexOfStr1InOriginalList,i)
            return indexAns

L = ["hello","this","is","yacoub"]
inStr = "hellois"



def strSearchV3(L,inStr):

    dict = {}
    indexNeeded1 = -1
    indexNeeded2 = -1
    for i in range(len(L)):
        dict[L[i]] = i
    for i in range(len(L)):
        firstSlice = inStr[:len(L[i])]
        secondSlice = inStr[len(L[i]):]
        if firstSlice in dict:
            indexOfFirst = dict[firstSlice]
            indexOfSecond = dict[secondSlice]
            return (indexOfFirst,indexOfSecond)
        if secondSlice in dict:
            indexOfFirst = dict[secondSlice]
            indexOfSecond = dict[firstSlice]
            return (indexOfSecond,indexOfFirst)
    return (-1,-1)

L = ["hello","this","is","yacoub"]
print(strSearchV3(L,inStr))

################################################################################
#### Problem 2 #################################################################
################################################################################

"""
Write a function minimum(L) which recursively calculates the minimum number in L
ASSUME IT IS NOT SORTED

mergeSort-> L = [4,5,5,7][0,1,3,9] L = [0,1,3,4,5,5,7,9]
2T(n/2) + O(n^0)
"""
def minimum(L):
    if len(L) == 2:
        return min(L[0],L[1]) #return the minimum of two elements
    if len(L) == 1:
        return L[0]
    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]
        left1 = minimum(left)
        right1 = minimum(right)
        return min(left1,right1)

"""
Problem 2.b) recurrence is 2T(n/2) + O(1)
since with each recursion we're dividing the list by half two times
and at the base case we're doing a O(1) operation
Applying Master's theorem leads to the time complexity being
O(n^(log2/log2)) == O(n)
"""

################################################################################
#### Problem 3 #################################################################
################################################################################

"""
write a function powerSet(L) which generates the powerset of a list L
L = ['a','b','c']
result = [[],['a'],['b'],['c'],['ab'],['bc'],['ac'],['abc']]

First level: [[]]
Second Level: ['a'],['b'],['c']
Third Level: ['ab'],['bc'],['ac']
Fourth Level: ['abc']

with every single element in every single level:
    1) do we add the element
    2) do we not add the element?

def powerSet(L):
    def powerSetRec(L,resultList,index):
        1) I'm going to add L[i] to the resultList
        2) I'm not going to add L[i] to the resultList
        [1.0,5.0,5.0,5.0,5.0]
        [1.0,2.0,3.0,4.0,5.0]
"""

import copy
def powerSet(L):
    if len(L) == 0:
        return [[]]
    x = powerSet(L[1:])
    y = copy.deepcopy(x)
    c = L[0]
    for i in range(len(y)):
        y[i] = [c] + y[i]
    return x+y
print(powerSet(['a','b','c']))
