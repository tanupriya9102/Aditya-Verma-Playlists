# Print Subsets | Print PowerSets | Print all Subsequences
def solve(ip, op):
    result = []
    if len(ip) == 0:
        result.append(op)
        return result  # Return the result immediately when the input is empty
    
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]  # Update the input by excluding the first character
    
    result += solve(ip, op1)  # Update the result by adding the recursive results
    result += solve(ip, op2)
    
    return result

print(solve("ab", ""))







