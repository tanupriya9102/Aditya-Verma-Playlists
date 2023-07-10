def lcp(ip,op):
     res=[]
     if len(ip)==0:
         res.append(op)
         return res
     op1=op2=op
     if ip[0].isdigit():
         op1+=ip[0]
         ip=ip[1:]
         res+=lcp(ip,op1)
     else:
         op1+=ip[0].upper()
         op2+=ip[0]
         ip=ip[1:]
         res+=lcp(ip,op1)
         res+=lcp(ip,op2)
     return res

    
print(lcp("a1b2",""))
