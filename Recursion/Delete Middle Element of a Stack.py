
def delete(s):
    if len(s)==0:
        return s
    else:
        k=len(s)//2+1
        solve(s,k)
        return s
def solve(s,k):
    if(k==1):
        s.pop()
        return s
    temp=s.pop()
    solve(s,k-1)
    s.append(temp)
    return s
s=[1,2,3,4,5]
print(delete(s))


        
    
