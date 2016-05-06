import teoria_numeros


class MasseyOmura:

    def __init__(self):
        self.c = 0
        self.d = 0
        self.q = 0

    def setCD(self, c):
        self.c = c
        self.d = c

    def setQ(self, q):
        self.q = q

    def encrypt(self, m):
        encrypt = teoria_numeros.exponenciacion(m, self.c, self.q)
        return encrypt

    def decrypt(self, encrypt):
        exp = teoria_numeros.inv(self.d, self.q)
        m = teoria_numeros.exponenciacion(encrypt, exp, self.q)
        return m
