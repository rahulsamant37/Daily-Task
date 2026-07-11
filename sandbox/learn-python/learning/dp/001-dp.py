## Without DP
calls = {}

def fibonicci_number_recursive(n):
    if (n not in calls):
        calls[n]=1
    else:
        calls[n]+=1
    if n<=1:
        return 1
    fib1 = fibonicci_number_recursive(n-1)
    fib2 = fibonicci_number_recursive(n-2)
    return fib1+fib2

# print(fibonicci_number_recursive(20))
# print(calls)


## With DP
dairy = [-1] * (20+1)
calls = {}
def fib_with_dp(n):
    if (n not in calls):
        calls[n]=1
    else:
        calls[n]+=1
    if n<=1:
        return 1
    if dairy[n]!=-1:
        return dairy[n]
    
    fib1 = fib_with_dp(n-1)
    fib2 = fib_with_dp(n-2)
    
    dairy[n-1] = fib1
    dairy[n-2] = fib2
    
    ans = fib1+fib2
    dairy[n]=ans
    return ans

print(fib_with_dp(20))
print(calls)