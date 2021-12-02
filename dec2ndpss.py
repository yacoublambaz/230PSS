################################################################################
################## Problem Solving Session 3 Questions #########################
################################################################################

"""
Problem 0.a (Difficulty 1/5)

Define a class Point, and contains two parameters x and y, representing the point
object.

Implement the initiation function (__init__)
Implement the __str__ function

make sure that the types of x and y are only limited to integers and floats
"""

class Point:
    def __init__(self,x=0,y=0):
        assert type(x) == int or type(x) == float, "Please enter floats or ints"
        self.x = x
        self.y = y
    def __str__(self):
        #returns a string
        strAns = "(" + str(self.x) + "," + str(self.y) + ")"

"""
Problem 0.b (Difficulty 1/5)

Define a class Rectangle, which requires two parameters Point1, and Point2
Where point1 represents the lower left corner
and point2 represents the upper right corner

Implement the initiation function (__init__)
Implement the __str__ function

make sure that the inputs are of type Point, and p.x <= q.x and p.y <= q.y
"""

class Rectangle:
    def __init__(self,p=Point(0,0),q=Point(0,0)):
        assert type(p) == Point and type(q) == Point, "incorrect data types"
        assert p.x <= q.x and p.y <= q.y, "incorrect point values"
        self.p = p
        self.q = q

    def height(self):
        return self.q.y - self.p.y

    def __str__(self):
        strAns = "( p = (" + str(self.p.x) + ", " + str(self.p.y) + ")" + ", " + ")"
        return strAns

    def extend(self,c):
        #extends the rectangle by multiplying the top right corner by c
        upperCorner = Point(self.q.x * c, self.q.y * c)
        return Rectangle(self.p, upperCorner)

rectangle1 = Rectangle(Point(2,4),Point(3,6))
#print(rectangle1.extend(3)) #return a rectangle object with upper right corner 9, 18


"""
Problem 1.a (Difficulty 2/5)

Given a list of integers, write a function threeSum(nums) that returns the indices
i,j,k of the three numbers in the list such that i!=j, j!=k, k!=i,
but nums[i] + nums[j] + nums[k] == 0.

nums[i] + nums[j] == -nums[k]

#Hint, write the two sum problem, then use that to help you solve it.
You should implement this solution in O(n^2) time complexity

The two sum problem goes as follows:
Given a list lst, return the indices of two numbers that add up to k

Steps:
1. Loop i through nums
2. Loop j through i,len(nums)
3. Loop through j, len(nums)

Naive solution:
for i in range(len(nums)):
    for j in range(i,len(nums)):
        for k in range(j,len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                return (i,j,k)
"""
def threeSum(nums):
    def twoSum(nums,k):
        dict = {}
        for i in range(len(nums)):
            if k-nums[i] in dict:
                return (dict[k-nums[i]],i)
            else:
                dict[nums[i]] = i
        return (-1,-1)

    for k in range(len(nums)):
        twoSum = twoSum(nums,-nums[k]) #is nums[i] + nums[j] == -nums[k]
        if twoSum != (-1,-1):
            return (k,twoSum[0],twoSum[1])
    return (-1,-1,-1)

L = [4,5,7,6,4,-10]
print(threeSum(L))





################################################################################
"""
Problem 2.a (Difficulty: 2/5):
This is an interview problem that I got just this week applying to a company.

Given a list of 0's and 1's, write a function sort(L) that returns the list
sorted with all zeroes to the right and all ones to the left.

Example:
L = [1,1,1,0,0,0] -> [0,0,0,1,1,1]
L = [1,0,1,0,0] -> [0,0,0,1,1]

Aim for a O(n) time complexity

Steps:
1. Implement counting problem on the list
2. Rebuild the list using the number of 0s and 1s that we got

"""
def sort(L):
    numOfZeros = 0
    numOfOnes = 0
    for elem in L: #O(n)
        if elem == 0:
            numOfZeros += 1 #increment / add
        else:
            numOfOnes += 1
    ansList = []
    for i in range(numOfZeros): #O(n)
        ansList.append(0)
    for i in range(numOfOnes): #O(n)
        ansList.append(1)
    return ansList #time complexity is O(3n) so O(n)

print(sort([0,0,0,1,0,0,1,1]))


################################################################################
"""
Problem 2.b (3/5):
Implement the sort() function in O(n) time complexity + O(1) space complexity.

O(1) space complexity means you are not allowed to create new lists or dictionaries
You are asked to solve this using only variables and loops.

numOfZeros = 0
numOfOnes = 0
for elem in L: #O(n)
    if elem == 0:
        numOfZeros += 1
    else:
        numOfOnes += 1
ansList = []
for i in range(numOfZeros): #O(n)
    ansList.append(0)
for i in range(numOfOnes): #O(n)
    ansList.append(1)
return ansList #time complexity is O(3n) so O(n)

L = [0,1,1,1,0,0,1]
i = expectedPositionOfZero
L = [0,0,1,1,1,0,1]
L = [0,0,0,1,1,1,1]

L = [1,1,1,1,0,0,0]

#Hint use swapping
"""

def sortEff(L):
    expectedPositionOfZero = 0
    for i in range(len(L)):
        if L[i] == 0:
            expectedPositionOfZero += 1
        else:
            break
    for i in range(expectedPositionOfZero+1,len(L)):
        if L[i] == 0:
            L[i], L[expectedPositionOfZero] = L[expectedPositionOfZero], L[i] #swapping
            expectedPositionOfZero+=1
    return L
#L = [0,1,1,1,0,0,0]
#L = [1,1,1,0,0,0]
L = [1,1,1,1,1,1]
print(sortEff(L))





################################################################################

"""
Problem 3 (Difficulty 4/5):

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Input:
n = 12:
Answer is 3. How? n = 12 is 4+4+4

n = 13:
Answer is 2. How? n = 13 is 9 + 4

Hint: Recursion

"""
def perfectSquare(n):
    #solve three problems:
    #1- how to count the depth of your tree in your recursive function
    #2- how to get the smallest of the depths in your recursive function?
    #3- how to recursively loop over a not-defined number of branches
    def perfSqRec(n,listOfSquares):
        if n < 0:
            return -1
        if n == 0:
            return 0
        else:
            currentMin = 1000
            for square in listOfSquares:
                branch = perfSqRec(n-square,listOfSquares)
                if branch != -1: #if the branch does lead to an answer
                    if branch < currentMin:
                        currentMin = branch
            return 1 + currentMin
    perfectSquareList = []
    for i in range(1,n):
        if i**2 > n:
            break
        else:
            perfectSquareList.append(i**2)
    return perfSqRec(n,perfectSquareList)

print(perfectSquare(30))

#first problem:
#my code is adding ALL branches that lead to 0

#second problem:
#I need to shortest path to get to 0


#step1:
#store the distances of the

################################################################################

"""
Problem 4: Difficulty (5/5)

Given n, return a list of all valid strings that have n open and n closed valid
paranthesis.

Eg:
N = 0 returns [‘’]
N = 1 returns [‘()’]
N = 2 returns [‘()()’,’(())’]
N = 3 returns [’()()()’, ’()(())’, ’(())()’, ’(()())’, ’((()))’]

This is an enumeration problem
Enumeration problems are by default difficulty 5/5
Luckily for us, they are very repetitive

"""

def allPara(n):
    if n == 0:
        return [""]
    ans = []
    for k in range(n): #if k == 2 and n == 5
        X = allPara(k) # k == 2
        Y = allPara(n-k-1) # 5 - 2 - 1 = 2
        for x in X:
            for y in Y:
                ansStr = "(" + x + ")" + y
                ans.append(ansStr)
    return ans




"""
Bonus Problem (Difficulty: 3/5):
I included this problem because my friend wanted to be included in the sessions.

Hadi Kibrit opened "AUB people" to see how many Kibrits are there at AUB.
To his surprise, Kibrits also write their name as Kebrit, Kibret, Kebret.
Not only do Kibrits do that, but Shirifs do that as well, among other family names.

Write a function generateNamePermutations(name) that return all possible permutations
of the name given.

You are not allowed to use the .replace() string method.
The problem is only restricted for i's and e's in the name. (For example,
Kashmar can also be written Keshmar, but we don't want to solve that here)

Eg:
Shirefee -> ["Shirifee","Sherifee","Shirefee","Sherefee"]

"""
def makeHadiFeelIncluded(famName):
    return []


"""

Bonus Problem 2 Difficulty (2/5):

Given a list L of numbers representing points on a line, find the distance between
closest pair of points

the distance between x1 and x2 is |x2-x1|

aim for O(nlogn)

"""

def getDistance(L):
    L.sort()
    currentMin = 1000
    for i in range(1,len(L)):
        if L[i] - L[i-1] < currentMin:
            currentMin = L[i] - L[i-1]
            pairOfPoints = (L[i],L[i-1])
    return pairOfPoints

print(getDistance([3,5,9,2]))
