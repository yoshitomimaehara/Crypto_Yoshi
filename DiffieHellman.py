import teoria_numeros


class DiffieHellman:

    def __init__(self):
        self.A = ""
        self.y = ""
        self.B = ""
        self.p = ""

    def setP(self, p):
        self.p = p

    def setA(self, A):
        self.A = A

    def setB(self, B):
        self.B = B

    def setY(self, y):
        self.y = y

    def encryptA(self):
        self.alpha = teoria_numeros.exponenciacion(self.y, self.A, self.p)
        return self.alpha

    def encryptB(self):
        self.beta = teoria_numeros.exponenciacion(self.y, self.B, self.p)
        return self.beta

    def decryptA(self):
        self.RA = teoria_numeros.exponenciacion(self.beta, self.A, self.p)
        return self.RA

    def decryptB(self):
        self.RB = teoria_numeros.exponenciacion(self.alpha, self.B, self.p)
        return self.RB