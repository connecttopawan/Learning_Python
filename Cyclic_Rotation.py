def solution(A, K):
    n=len(A)
    if (n>0):
        for j in range(K):
            temp=A[n-1]
            for i in range(n-1):
                A[n-1-i]=A[n-2-i]
            A[0]=temp
        return A
    else:
        return A