# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
stack=[]
for _ in range(n):
    queries=list(map(int, input().split()))
    #print ("int : ",int," split : ",list((input().split())))
    #print (queries)
    if (queries[0]==1):
        if (stack):
            stack.append(max(stack[-1],queries[1]))
        else:
            stack.append(queries[1])
    elif (queries[0]==2):
        if (stack):
            stack.pop()
    else:
        if (stack):
            print(stack[-1])
            
    