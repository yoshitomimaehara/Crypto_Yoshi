import teoria_numeros
import random


class ElgamalLargo:

    def __init__(self):
        self.p = 0
        self.g = 0
        self.a = 0
        self.r = 0

    def setA(self, a):
        self.a = a

    def setN(self, n):
        self.n = n

    def setG(self, g):
        self.g = g

    def setP(self, p):
        self.p = p

    def setR(self, r):
        self.r = r

    # no se me ocurre
    def obtainP(self):
        #self.p = f * q
        pass

    def cantBits(self):
        i = 0
        k = 0
        while k < self.p:
            k = (255 * 256 ** i) + k
            i = i + 1

    def generateG(self):
        while teoria_numeros.exponenciacion(self.g, 2, self.p - 1) == 1:
            self.g = teoria_numeros.raizprimitiva(self.p - 1)

    def generateA(self):
        self.a = random.randrange(1, (self.p - 1))

    def generateR(self):
        self.r = random.randrange(1, (self.p - 1))

    def getPublicKey(self):
        r = teoria_numeros.exponenciacion(self.g, self.a, self.p)
        return r

    def encrypt(self, message):
        res1 = teoria_numeros.exponenciacion(self.g, self.r, self.p)
        temp = self.getPublicKey()
        oper = teoria_numeros.exponenciacion(temp, self.r, self.p)
        res2 = (message * oper) % self.p
        return [res1, res2]

    def decrypt(self, encrypt):
        res = teoria_numeros.exponenciacion(encrypt[0], self.a, self.p)
        res2 = teoria_numeros.inv(res, self.p)
        m = (encrypt[1] * res2) % self.p
        return int(m)