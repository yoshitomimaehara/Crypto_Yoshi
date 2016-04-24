import random
import teoria_numeros


class Elgamal:

    def __init__(self):
        self.p = 0
        self.g = 0
        self.a = 0
        self.r = 0
        self.ga = 0

    def setA(self, a):
        self.a = a

    def setN(self, n):
        self.n = n

    def setG(self, g):
        self.g = g

    def setP(self, p):
        self.p = p

    def setGA(self, ga):
        self.ga = ga

    def setR(self, r):
        self.r = r

    # no se me ocurre
    def obtainP():
        #self.p = f * q
        pass

    def generateG(self):
        while teoria_numeros.exponenciacion(self.g, 2, self.p) == 1:
            self.g = teoria_numeros.raizprimitiva(self.p)

    def generateA(self):
        self.a = random.randrange(2, (self.p - 2))

    def generateR(self):
        self.r = random.randrange(2, (self.p - 2))

    def getPublicKey(self):
        self.ga = teoria_numeros.exponenciacion(self.g, self.a, self.p)

    def encrypt(self, message):
        res1 = teoria_numeros.exponenciacion(self.g, self.r, self.p)
        oper = teoria_numeros.exponenciacion(self.ga, self.r, self.p)
        res2 = (message * oper) % self.p
        return [res1, res2]

    def decrypt(self, encrypt):
        res = teoria_numeros.exponenciacion(encrypt[0], self.a, self.p)
        res2 = teoria_numeros.inv(res, self.p)
        m = (encrypt[1] * res2) % self.p
        return int(m)


if __name__ == "__main__":
    ga = Elgamal()
    gb = Elgamal()
    #gc = Elgamal()
    ga.setP(71)
    gb.setP(71)
    #gc.setP(37)
    #ga.generateG()
    ga.setG(7)

    #ga.generate(a)
    ga.setA(26)
    #ga.setGA(3)
    #ga.generateR()
    ga.setR(73)
    ga.getPublicKey()
    print((ga.encrypt(30)))
    #print((ga.decrypt([131, 45])))