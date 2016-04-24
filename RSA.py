import random
import teoria_numeros


class RSA:

    def __init__(self):
        self.p = ""
        self.q = ""
        self.n = ""
        self.totient = ""

    def messagePartitions(self, message, r):
        partitions = []
        j = 0
        temp = ""
        for i in range(0, len(message)):
            temp = temp + message[i].upper()
            j = j + 1
            if j == r:
                partitions.append(temp)
                temp = ""
                j = 0

        return partitions

    def getAlpha(self):
        alpha = {}
        f = open("alfabeto.alf", "r")
        temp1 = f.readline()
        while temp1:
            temp = temp1.split(" => ")
            temp1 = f.readline()
            alpha[temp[0]] = temp[1].rstrip("\n")
        f.close()
        return alpha

    def getFirstkeyAlpha(self):
        alpha = list(self.getAlpha().keys())
        return alpha[0]

    def getLenghtalphaKey(self):
        alpha = self.getAlpha()
        return len(alpha[self.getFirstkeyAlpha()])

    def getP(self):
        return self.p

    def setPQ(self, p, q):
        self.p = p
        self.q = q

    def getQ(self):
        return self.q

    def eulerSpecial(self):
        return (self.p - 1) * (self.q - 1)

    def setN(self, n):
        self.n = n

    def getN(self):
        if (self.p != "" and self.q != "") and self.n == "":
            self.n = self.p * self.q

        return self.n

    def euler(self):
        if self.p != "" and self.q != "":
            self.totient = self.eulerSpecial()
        elif self.n != "":
            self.totient = teoria_numeros.euler(self.n)

    def getTotient(self):
        return self.totient

    def generatePrimes(self, tam):
        self.p = random.randrange(10 ** tam, 10 ** (tam + 1) - 1)
        self.q = random.randrange(10 ** tam, 10 ** (tam + 1) - 1)

    def generatePublickey(self, tam):
        self.euler()
        e = random.randrange(0, 10 ** (tam + 1) - 1)
        while teoria_numeros.mcd(e, self.getTotient()) != 1:
            e = random.randrange(0, 10 ** (tam + 1) - 1)

    def setPublickey(self, e):
        self.e = e

    def getPublickey(self):
        return self.e

    def getPrivatekey(self):
        self.euler()
        self.d = teoria_numeros.inv(self.getPublickey(), self.getTotient())
        return self.d

    def toDigits(self, partitions, r):
        result = []
        temp = ""
        j = 0
        alfabeto = self.getAlpha()
        for i in range(0, len(partitions)):
            tempMat = partitions[i]
            for k in range(0, len(tempMat)):
                temp = temp + alfabeto.get(tempMat[k])
                j = j + 1
                if j == r:
                    result.append(temp)
                    temp = ""
                    j = 0

        return result

    def toChara(self, partitions):
        result = ""
        keys = []
        alfabeto = self.getAlpha()
        keys = sorted(alfabeto.keys())
        for i in range(0, len(partitions)):
            for j in range(0, len(keys)):
                if alfabeto.get(keys[j]) == partitions[i]:
                    result = result + keys[j]

        return result

    def encrypt(self, message, r):
        result1 = []
        result = ""
        temp2 = ""
        if (self.p == "" and self.q == "") and self.n == "":
            tam = eval(input("Write prime's size: '"))
            self.generatepq(tam)

        e = self.getPublickey()
        n = self.getN()
        temp = self.messagePartitions(message, r)
        N = self.toDigits(temp, r)
        print(N)
        for i in range(0, len(temp)):
            expo = teoria_numeros.exponenciacion(int(N[i]), e, n)
            temp2 = str(expo)
            if len(temp2) == 1:
                temp2 = '0' + temp2
            result1.append(temp2)
            result = result + temp2
        print(result1)

        return result

    def decrypt(self, encrypt, r):
        result = []
        temp = []
        temp3 = []
        temp2 = ""
        j = 0
        d = self.getPrivatekey()
        for i in range(0, len(str(encrypt))):
            temp2 = temp2 + encrypt[i]
            j = j + 1
            if j == self.getLenghtalphaKey():
                cast = int(temp2)
                expo = teoria_numeros.exponenciacion(cast, d, self.getN())
                temp.append(expo)
                temp2 = ""
                j = 0

        for j in range(0, len(temp)):
            temp1 = str(temp[j])
            if len(temp1) == 1:
                temp1 = '0' + temp1
            temp3.append(temp1)

        print(temp3)
        result = self.toChara(temp3)

        return result


if __name__ == "__main__":
    #A = RSA()
    B = RSA()
    rsa = RSA()
    part = rsa.messagePartitions("H", 1)
    print(part)
    #A.setN(35)
    B.setPQ(3, 11)
    #print((B.getN()))
    #A.setPublickey(5)
    B.setPublickey(3)
    #print((A.getPrivatekey()))
    #print((B.getPrivatekey()))
    #print((A.encrypt("HOLA", 1)))
    print((B.decrypt('08111701', 1)))
    #print rsa.getAlpha().get('B')
    print((rsa.toDigits(part, 1)))
    #print rsa.toChara(["01"],2)
    #print rsa.eulerSpecial()
    #print rsa.getPrivatekey()
    #print teoria_numeros.exponenciacion(8,5,35)