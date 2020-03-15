def genPrimes():
    primes = []
    if len(primes) == 0:
        primes.append(2)
        yield 2
    siguiente = primes[-1]+1
    while True:
        esPrimo = True
        for primo in primes:
            if (siguiente % primo == 0):
                esPrimo = False
                break
        if esPrimo:
            primes.append(siguiente)
            yield siguiente
        else:
            siguiente += 1
                
    
