def tobase(n, base):
    new = 0
    place = 1
    while n > 0:
        new += (n % base) * place
        n //= base
        place *= 10
    return new
