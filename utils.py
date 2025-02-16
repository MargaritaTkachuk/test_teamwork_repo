 if n<2 return False

def tobase(n, base):
    new = 0
    place = 1
    while n > 0:
        new += (n % base) * place
        n //= base
        place *= 10
    return new

def step_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1