## Recrurtion ka mtlb hm ek function k ander usi function ko call kr rhe h pr dusre artribute k sath
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
def fibonacchi(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacchi(n-1) + fibonacchi(n-2)
print(fibonacchi(6))