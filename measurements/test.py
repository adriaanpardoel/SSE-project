import energyusage

# user function to be evaluated
def recursive_fib(n):
    if (n <= 2): return 1
    else: return recursive_fib(n-1) + recursive_fib(n-2)

energyusage.evaluate(recursive_fib, 40, pdf=True)
# returns 102,334,155
