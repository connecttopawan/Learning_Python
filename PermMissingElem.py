# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)+1
    if (n>0 and n <1000000):
        result = n * (n + 1)//2
        #print (result)
        return result - sum(A)
    else:
        return 1
    
