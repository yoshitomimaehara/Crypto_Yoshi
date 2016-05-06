import random
import math


def tobase2(n):
    bina = []
    q = -1
    while q != 0:
        q = n // 2
        r = n % 2
        bina.append(r)
        n = q

    while len(bina) < 8:
        bina.append(0)

    bina.reverse()
    return bina


def exponenciacion(a, b, n):
    bina = []
    bina = tobase2(b)
    x = 1
    k = 0
    while k < len(bina):
        if bina[k] == 0:
            x = (x ** 2) % n
        elif bina[k] == 1:
            x = (x ** 2 * a) % n
        k = k + 1
    return x


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def mcd(a, b):
    c = abs(a)
    d = abs(b)
    while d != 0:
        r = c % d
        c = d
        d = r
    return c


def esmultiplo(n, a):
    if n % a == 0:
        return True
    else:
        return False


def descomposicion2expo(n):
    result = []
    # p - 1 = 2 ** u * r
    # r es impar
    num = n - 1
    u = 0
    while num % 2 == 0:
        num = num / 2
        u = u + 1

    r = num

    result.append(u)
    result.append(int(r))

    return result


### Extraido de https://gist.github.com/bnlucas/
#Check
def check(a, s, d, n):
    x = pow(a, d, n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return x == n - 1


# test de Miller Rabin
def esprimo(n, k=20):
    if n == 2 or n == 3:
        return True
    # comprueba si es par
    if not n & 1:
        return False

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True
###


#test de Fermat
def esprimo_little(n):
    r = ""
    if n > 3:
        cant = n - 1
        a = random.randrange(2, cant, 1)
        while mcd(a, n) == 0:
            a = random.randrange(2, cant, 1)

        if mcd(a, n) == 1 and exponenciacion(a, n - 1, n) == 1:
            r = True
        else:
            r = False
    elif n == 3 or n == 2:
        r = True
    return r


def bezout(a, b):
    result = []
    c = abs(a)
    d = abs(b)
    c1 = 1
    d1 = 0
    c2 = 0
    d2 = 1
    while d != 0:
        q = c // d
        r = c - q * d
        r1 = c1 - q * d1
        r2 = c2 - q * d2
        c = d
        c1 = d1
        c2 = d2
        d = r
        d1 = r1
        d2 = r2
    t = c1 / (sgn(a) * sgn(c))
    s = c2 / (sgn(b) * sgn(c))
    result.append(c)
    result.append(s)
    result.append(t)
    return result


def orden(a, m):

    if m <= 1:
        return 0
    assert mcd(a, m) == 1
    z = a
    r = 1
    while z != 1:
        z = (z * a) % m
        r = r + 1

    return r


def factorizacion(n):
    factores = []
    i = 1
    r = n
    while i <= (math.sqrt(n) + 1):
        if esprimo_little(i) is True and r % i == 0:
            factores.append(i)
            r = r / i
        else:
            i = i + 1
    if r > 1:
        factores.append(int(r))
    return factores


def factorizacion_primos_unica(n):
    factores = []
    i = 1
    r = n
    while i <= (int(math.sqrt(n)) + 1):
        if esprimo_little(i) is True and r % i == 0:
            factores.append(i)
            r = r / i
        i = i + 1

    return factores


#algoritmo de Shanks
def logdiscreto(alpha, beta, p):
    result = []
    if alpha == -1:
        alpha = generador(p)
    m = int(math.ceil(math.sqrt(p - 1)))
    num = [i for i in range(0, m)]

    A = dict.fromkeys(num)
    for j in range(0, m):
        A[j] = exponenciacion(alpha, m * j, p)

    print(A)

    B = dict.fromkeys(num)

    for i in range(0, m):
        base = inv(alpha, p)
        B[i] = beta * exponenciacion(base, i, p) % p

    print(B)

    for i in range(0, m):
        for j in range(0, m):
            if A.get(j) == B.get(i):
                a = m * j + i
                result.append(a)

    return result


def primosmenores(n):
    result = []
    for i in range(1, n):
        if esprimo_little(i):
            result.append(i)
    return result


def euler(n):
    primos = []
    if esprimo(n) is True:
        totient = n - 1
    else:
        primos = factorizacion_primos_unica(n)
        i = 0
        prod = 1
        while i < len(primos):
            calcpar = (float(1) - (float(1) / float(primos[i])))
            prod = float(prod) * calcpar
            i = i + 1
        totient = n * prod
    return totient


def inv(a, b):
    result = bezout(a, b)
    inv = result[2]
    #k = 1
    if(inv < 0):
        while inv < 0:
            #k = k + 1
            #b = b * k
            inv = inv + b
    return inv


# extraido de ent_py
# http://igm.univ-mlv.fr/~jyt/Crypto/4/ent.py
def raizprimitiva(p):

    if p == 2:
        return 1
    F = factorizacion(p - 1)
    a = 2
    while a < p:
        generates = True
        for q, _ in F:
            if exponenciacion(a, (p - 1) / q, p) == 1:
                generates = False
                break
        if generates:
            return a
        a += 1
    assert False, "p must be prime."


### Corregir
def generador(n):
    table = {}
    p = []
    temp = []
    num = primosmenores(n)
    totient = int(euler(n))

    if n == 2:
        return 1

    cant = euler(totient)
    print(("euler = " + str(totient)))
    print(("Cant generadores = " + str(int(cant))))

    for i in range(0, len(num)):
        if totient % num[i] == 0:
            p.append(num[i])

    table = dict.fromkeys(p)
    for i in range(0, len(p)):
        k = 0
        for j in range(1, totient):
            if exponenciacion(j, (totient / p[i]), n) != 1:
                if k < int(cant):
                    temp.append(j)
                    k = k + 1
            if len(temp) == int(cant):
                table[p[i]] = temp
    return table


def jacobi(a, n):
    assert n >= 3
    assert n % 2 == 1
    a = a % n
    if a == 0:
        return 0
    if a == 1:
        return 1
    a1, e = a, 0
    while a1 % 2 == 0:
        a1, e = a1 // 2, e + 1
    if e % 2 == 0 or n % 8 == 1 or n % 8 == 7:
        s = 1
    else:
        s = -1
    if a1 == 1:
        return s
    if n % 4 == 3 and a1 % 4 == 3:
        s = -s
    return s * jacobi(n % a1, a1)


def raizcuadradaprima(a, n, b=0):
    l = []
    d = []
    r = []
    c = []
    s = 0
    assert jacobi(a, n) == 1

    for k in range(0, n):
        if jacobi(k, n) == -1:
            l.append(k)
    if b == 0:
        b = random.choice(l)
   # print(("b = " + str(b)))
    temp = descomposicion2expo(n)
    s = temp[0]
    # print(("s = " + str(s)))
    t = temp[1]
    # print(("t = " + str(t)))

    ap = inv(a, n)
    d.append(0)
    c.append(exponenciacion(b, t, n))
    r.append(exponenciacion(a, ((t + 1) / 2), n))
    for i in range(1, s):
        d.append(exponenciacion((r[i - 1] ** 2) * ap, (2 ** (s - i - 1)), n))
        if d[i] % n == n - 1:
            r.append((r[i - 1] * c[i - 1]) % n)
        else:
            r.append(r[i - 1])

        c.append(exponenciacion(c[i - 1], 2, n))

   # for i in range(0, s):
        #print((str(int(d[i])) + " " + str(r[i]) + " " + str(c[i])))

    #return [r[s - 1], -r[s - 1]]
    return [r[s - 1], -r[s - 1] + n]


def raizcuadradacompuesta(a, p, q, b=0):

    rr = raizcuadradaprima(a, p, b)
    print(rr)
    rs = raizcuadradaprima(a, q, b)
    print(rs)

    n = p * q

    #r = rr[0]
    #s = rs[0]

    ap = (q * inv(q, p)) % n
    #print(("a' = " + str(ap)))
    aq = (p * inv(p, q)) % n

    x = (ap * rr[1] + aq * rs[1]) % n

    y = (ap * rr[0] - aq * rs[0]) % n

    return [x, -x, y, -y]


def reciprocidad(p, q):
    assert p != q
    assert esprimo(p)
    assert esprimo(q)

    p1 = p
    q1 = q
    e = 1
    while (q1 % p1 != 1):
        e = (-1) ** (((p1 - 1) * (q1 - 1)) / 4) * e
        temp = p1
        p1 = q1 % temp
        q1 = temp

    r = e * (q1 % p1)

    return r


def legendre(a, p):
    if p < 2:
        raise ValueError('p must not be < 2')
    if (a == 0) or (a == 1):
        return a
    if a % 2 == 0:
        r = legendre(a / 2, p)
        if p * p - 1 % 8 != 0:
            r *= -1
    else:
        r = legendre(p % a, a)
        if (a - 1) * (p - 1) % 4 != 0:
            r *= -1
    return r


if __name__ == "__main__":

    #print ((tobase2(2)))
    #print ((exponenciacion(6, 9, 7)))
    #print ((mcd(148, 40)))
    #print ((bezout(78, 32)))
    #print ((orden(3, 37)))
    #print ((esprimo(37)))
    #print ((esprimo_little(11)))
    #print ((factorizacion(7)))
    #print ((esprimo(91, 4)))
    #print ((euler(36)))
    #print ((inv(3, 13)))
    #print ((exponenciacion(13,2,37)))
    #print ((factorizacion_primos_unica(6)))
    #print ((logdiscreto(7, 57, 71)))
    #print ((primosmenores(37)))
    print ((generador(2)))
    #print ((descomposicion2expo(97)))
    #print ((jacobi(7, 23)))
    #print ((raizcuadradaprima(132, 17, 14)))
    #print ((reciprocidad(11, 77)))
    #print ((legendre(7 , 23)))
    #print ((raizcuadradacompuesta(23, 7, 11, 9)))

    """
    for i in range(1, 37):
        print i + " " + exponenciacion(i,(36/2),37)
    """
    """
    for k in range(4, 97):
        print ((reciprocidad(k, 97)))
    """

    #invb = inv(21, 37)
    #print((30 * invb) % 37)
    #print ((logdiscreto(5, 25, 37)))
