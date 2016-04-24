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

if __name__ == "__main__":
    A = MasseyOmura()
    B = MasseyOmura()
    A.setQ(53)
    B.setQ(53)
    A.setCD(3)  # en realidad este es c
    B.setCD(7)  # en realidad este es d
    p1 = A.encrypt(13)
    print(p1)
    p2 = B.encrypt(p1)
    print(p2)
    p3 = A.decrypt(p2)
    print(p3)
    p4 = B.decrypt(p3)
    print(p4)