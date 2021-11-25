################################################################################
################## Problem Solving Session 2 Questions #########################
################################################################################


"""

Problem 1.a (Difficulty: 1/5):
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.

examples:
s = "Hello World" -> len(World) is 5
s = "   fly me   to   the moon  " -> len(moon) is 4

First, solve this normally, then solve it using a single line of code

Bonus:
Implement lenOfLast(s) without the split() function difficulty 3/5

"""
def lenOfLast(s):
    return s.split()[len(s.split())-1]



################################################################################
"""
Problem 2.a (Difficulty: 2/5):
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps at a time. How many distinct ways
can you climb the stairs to reach the top?

Hint) recursion 1

Eg:
n = 2 -> 2 ways -> 1 + 1, 2
n = 3 -> 3 ways -> 1 + 1 + 1, 2+1, 1+2

What is the time complexity of this solution?
"""
def climb(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return climb(n-1) + climb(n-2)



################################################################################
"""
Problem 2.b (3/5):
Implement the climbStairs problem in O(n)
Hint: memoization
"""
def climbFast(n): #wrapper
    def climbFastMem(n,L): #recursive
        #1- is this problem a problem that I have solved before?
        if L[n] != -1:
            return L[n]
        #2- is this a base case?
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n > 0:
            #3- Not a base case, so solve and put in the list
            L[n] = climbFastMem(n-1,L) + climbFastMem(n-2,L)
            return L[n]

    L = [-1]*(n+1)
    return climbFastMem(n,L)

################################################################################
"""
Problem 4 (4/5):
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

# 1- loop over the grid to find the first letter
# 2- from the first letter as the starting point, implement maze traversal

board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]]
word = "ABCCED"
result is True

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "CCE"

"""
def findInMaze(board,word):
    def maze(board,replica,i,j,wordNeeded,wordSoFar):
        if not replica[i][j]: #is this i,j a cell that I haven't visited before?
            replica[i][j] = True #mark it as visited
            if wordSoFar == wordNeeded:
                return True
            if len(wordSoFar) > len(wordNeeded):
                return False
            left = False
            up = False
            right = False
            bot = False
            if i > 0:
                left = maze(board,replica,i-1,j,wordNeeded,wordSoFar+board[i-1][j])
            if j > 0:
                up = maze(board,replica,i,j-1,wordNeeded,wordSoFar+board[i][j-1])
            if i < len(board)-1:
                right = maze(board,replica,i+1,j,wordNeeded,wordSoFar+board[i+1][j])
            if j < len(board[i])-1:
                bot = maze(board,replica,i,j+1,wordNeeded,wordSoFar+board[i][j+1])
            return left or right or up or bot #if any of them is true, return true
        else:
            return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                replica = [[False for i in range(len(board[0]))] for i in range(len(board))]
                isExist = maze(board,replica,i,j,word,board[i][j])
                if isExist:
                    return True
    return False



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "CCE"
print(findInMaze(board,word))

################################################################################

"""
Problem 5: Difficulty (5/5)
Write a function genStr(n), which given n, returns a list of all length n
strings that have abc in them, but in a way that no two letters are
repeated consecutively. For example, abca is allowed but aabc is not allowed.
genStr(0) returns [‘’]
genStr(1) returns [‘a’,’b’,’c’]
genStr(2) returns [’ab’, ’ac’, ’ba’, ’bc’, ’ca’, ’cb’]
genStr(3) returns [’aba’, ’abc’, ’aca’, ’acb’, ’bab’, ’bac’, ’bca’,
’bcb’, ’cab’, ’cac’, ’cba’, ’cbc’]

This is an enumeration problem
Enumeration problems are by default difficulty 5/5
Luckily for us, they are very repetitive

"""

def genStr(n):
    if n < 0:
        return []
    if n == 0:
        return [""]
    X = genStr(n-1)
    ans = []
    for element in X:
        for letter in ["a","b","c"]:
            if len(element) > 0:
                if element[len(element)-1] != letter:
                    ans.append(element+letter)
            else:
                ans.append(element+letter)
    return ans
print(genStr(4))


"""
Bonus Problem (Difficulty: 4/5)
Given a string s and a list of strings wordLst,
return true if s can be segmented into a sequence
of one or more list words.

Examples:
s = "yacoublambaz", wordLst = ["yacoub","lambaz"]
-> True, "yacoublambaz" = "yacoub" + "lambaz"

s = "catsanddogs", wordLst = ["cats","sand","dogs"]
-> False

s = "applepenapple", wordLst = ["apple","pen"]
-> True, "applepenapple" = "apple" + "pen" + "apple"
"""
def wordBreak(word,lst):
    return 0
