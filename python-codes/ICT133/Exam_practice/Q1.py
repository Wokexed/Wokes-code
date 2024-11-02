# Qn 1aiii)
def isPrime(n):

    if i < 2:
        return False
    for i in range(2, n):
        if n % i != 0:
            return False
    return True       
            
    
isPrime(11)
isPrime(12)
isPrime(21)

