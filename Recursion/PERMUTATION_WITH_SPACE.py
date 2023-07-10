#when no space required befre 1st letter of string "ABC" => NO SPACE BEFORE A


# helper function
def pws(ip,op):
     res=[]
     if len(ip)==0:
         res.append(op)
         return res
     op1=op2=op
     op1+=ip[0]
     op2+="_"
     op2+=ip[0]
     ip=ip[1:]
     res+=pws(ip,op1)
     res+=pws(ip,op2)
     return res


# this is the function to be called in main   
def solve(init_ip):
    ip=init_ip[1:] 
    op=init_ip[0]
    return pws(ip,op)
    
print(solve("ABC"))
        
    
