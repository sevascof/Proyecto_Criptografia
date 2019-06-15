import time
start = time.time()

def isNotPrime(possible):
    i = 2
    while i*i <= possible:
        if (possible % i) == 0:
            return True
        i = i + 1
    return False


def primRoots(theNum):
    if isNotPrime(theNum):
        raise ValueError("Sorry, the number must be prime.")
    o = 1
    roots = []
    r = 2
    while r < theNum:
        k = pow(r, o, theNum)
        while (k > 1):
            o = o + 1
            k = (k * r) % theNum
        if o == (theNum - 1):
            roots.append(r)
        o = 1
        r = r + 1
    return roots


num = input("Ingrese valor: ")
print(primRoots(int(num)))
end = time.time()
print("\nCódigo ejecutado en {} segundos".format(end - start))