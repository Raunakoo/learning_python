'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given

scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n
. The second line contains an array of A[] of n integers each separated by a space.

Constraints

Output Format

Print the runner-up score.
'''
n = int(input("n? "))
print("this is n", n)

#############################################################################
#map(func, *iterables) --> map object
#Make an iterator that computes the function 
# using arguments from each of the iterables. 
# Stops when the shortest iterable is exhausted.
#############################################################################
##str.split(sep=None, maxsplit=-1) -> list
##Return a list of the words in S, using sep as the delimiter string. 
## If maxsplit is given, at most maxsplit splits are done. 
## If sep is not specified or is None, any whitespace string is a separator
## and empty strings are removed from the result
#############################################################################

arr = map(int, input("arr? ").split())
print("this is arr", arr)