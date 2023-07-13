# N-bit binary numbers having more 1’s than 0’s for any prefix

def NBitBinary(n):
    op=""
    res=[]
    def helper(n,o,z,op,res):
        if o+z==n:
            res.append(op)
            return res
        if o!=n:
            helper(n,o+1,z,op+'1',res)
        if o>z:
            helper(n,o,z+1,op+'0',res)
        return 
    helper(n,0,0,op,res)
    return res
    
print(NBitBinary(3))
