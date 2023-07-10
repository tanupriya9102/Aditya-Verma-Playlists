
def pwc(ip,op):
     res=[]
     if len(ip)==0:
         res.append(op)
         return res
     op1=op2=op
     op1+=ip[0].upper()
     op2+=ip[0]
     ip=ip[1:]
     res+=pwc(ip,op1)
     res+=pwc(ip,op2)
     return res

    
print(pwc("ab",""))
        
    
