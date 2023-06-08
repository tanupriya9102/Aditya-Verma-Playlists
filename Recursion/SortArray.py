def Mysort(l):
    if(len(l)==1):
        return l
    temp=l.pop() #remove last element to place it at right pos
    Mysort(l) #recursively sort rest of the array
    insert(l,temp) #induction step for insertion of last element
    return l

def insert(l,temp):
    if(len(l)==0 or l[-1]<=temp):
        l.append(temp)
        return l
    x=l.pop()
    insert(l,temp)
    l.append(x)
    return l
    
l=[6,0,5,7,1,2]
print(Mysort(l))
    
