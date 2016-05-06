import teoria_numeros
import random


class Rabin:

    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.b = 0

    def setPublicKey(self, n):
        self.n = n

    def setB(self, b):
        self.b = b

    def generateB(self):
        self.b = random.randrange(0, self.n - 1)

    def generatePQ(self):
        fact = self.getPrivateKey()
        self.p = fact[0]
        self.q = fact[1]

    def getPrivateKey(self):
        fact = teoria_numeros.factorizacion(self.n)
        return fact

    def encrypt(self, M):
        C = (M ** 2 + self.b * M) % self.n
        return C

    def decrypt(self, C):
        CR = []  # conjunto de Raices
        PM = []  # Posibles M
        self.generatePQ()
        base = ((self.b ** 2) * teoria_numeros.inv(4, self.n)) + C
        CR = teoria_numeros.raizcuadradacompuesta(base, self.p, self.q, self.b)
        print(CR)
        temp = self.b * teoria_numeros.inv(2, self.n)
        for i in range(0, len(CR)):
            PM.append((CR[i] - temp) % self.n)
        print(PM)
