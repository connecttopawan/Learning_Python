# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n=len(A)
    d={}
    flag=0
    if (n>0):
        for i in range (n-1):
            count=1
            for j in range (i+1,n):
                if(A[i]==A[j] and A[i]<=1000000000):
                    count=count+1
                    #print (count)
            if A[i] not in d:
                d[A[i]]=count
        #print(d)
        for key in d:
            if (d[key]%2==0):
                flag=1
                break
        for key in d:
            if (d[key]%2!=0 and d[key]<=1000000 and flag==1):
                #print(key)
                return key