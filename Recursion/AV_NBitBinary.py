def NBitBinary(n):
    op=""
    res=[]
    def helper(n,o,z,op,res):
        if n==0:
            res.append(op)
            return res
        if o>z:
            helper(n-1,o,z+1,op+'0',res)
        helper(n-1,o+1,z,op+'1',res)
        return 
    helper(n,0,0,op,res)
    return res
    
print(NBitBinary(3))
