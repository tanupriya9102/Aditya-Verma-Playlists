def genParanthesis(n):
    op=""
    res=[]
    def helper(o,c,op,res):
        if o==0 and c==0:
            res.append(op)
            return res
        if o!=0:
            helper(o-1,c,op+'(',res)
        if c>o:
            helper(o,c-1,op+')',res)
        return 
    helper(n,n,op,res)
    return res
    
print(genParanthesis(3))
        
            
