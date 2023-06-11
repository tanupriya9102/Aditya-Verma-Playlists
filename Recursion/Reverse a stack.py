# 2 functions resverse a stack and insert in stack (insert is helper function)

def reverse(s):
    if len(s)==1: #BC
        return s
    ele=s.pop()
    reverse(s)
    insert(s,ele)
    return s
    
def insert(s,ele):
    if len(s)==0: #BC
        s.append(ele)
        return s
    temp=s.pop()
    insert(s,ele)
    s.append(temp)
    return s
    
s=[1,2,3,4,5]
print(reverse(s))

    
