import random
import teoria_numeros


class MerkleHellman:

    def __init__(self):
        self.m = 0
        self.mu = 0
        self.w = 0
        self.winv = 0
        self.s = []
        self.pubkey = []
        self.privkey = []

    def tobase2(self, n):
        bina = []
        q = -1
        while q != 0:
            q = n // 2
            r = n % 2
            bina.append(r)
            n = q
        bina.append(0)
        bina.append(0)
        bina.reverse()
        return bina

    def tobase10(self, n):
        dec = []
        for i in range(len(n)):
            k = n[i]
            s = 0
            for j in range(len(k)):
                s = s + ((2 ** j) * k[j])
            dec.append(str(s))
        return dec

    def messagePartitions(self, message, r):
        partitions = []
        j = 0
        temp = ""
        for i in range(0, len(message)):
            temp = temp + message[i]
            j = j + 1
            if j == r:
                partitions.append(temp)
                temp = ""
                j = 0

        return partitions

    def getAlpha(self):
        alpha = {}
        f = open("ascii.alf", "r")
        temp1 = f.readline()
        while temp1:
            temp = temp1.split(" => ")
            temp1 = f.readline()
            alpha[temp[0]] = temp[1].rstrip("\n")
        f.close()
        return alpha

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

    def setMu(self, mu):
        self.mu = mu

    def setM(self, m):
        self.m = m

    def setW(self, w):
        self.w = w

    def getWinverse(self):
        self.winv = teoria_numeros.inv(self.w, self.mu)
        return int(self.winv)

    def setMochilasimple(self, mochila):
        self.s = mochila

    def generateW(self):
        while teoria_numeros.mcd(self.w, self.mu) != 1:
            x = random.randrange(2, self.mu - 2)
            r = teoria_numeros.mcd(self.mu, x)
            self.w = x // r

    def getBits(self):
        bits = 2 * self.m + 2
        print(("Bits : " + str(bits)))
        return bits

    def generateMu(self):
        self.mu = random.randrange(2 ** (2 * self.m + 1) + 1,
                    2 ** (2 * self.m + 2) - 1)

    def generateMochilasimple(self):
        for i in range(1, self.m):
            start = (2 ** (i - 1) - 1) * 2 ** self.m + 1
            end = 2 ** (i - 1) * 2 ** self.m
            s = random.randrange(start, end)
            self.mochilasimp.append(s)

    def getPublicKey(self):
        for i in range(0, len(self.s)):
            self.pubkey.append((self.s[i] * self.w) % self.mu)
        return self.pubkey

    def getPrivateKey(self):
        self.getWinverse()
        return [self.mu, int(self.winv)]

    def messagetobin(self, message):
        binary = []
        partitions = self.messagePartitions(message, 1)
        for i in range(len(partitions)):
            codigo = int(self.toDigits(partitions[i], 1)[0])
            binary.append(self.tobase2(codigo))
        return binary

    def messagebinunion(self, messagebin):
        result = ""
        for i in range(len(messagebin)):
            temp = messagebin[i]
            for j in range(len(temp)):
                result = result + str(temp[j])

        return result

    def codetobinpartic(self, encrypt):
        mochinver = self.s
        mochinver.reverse()
        result = []
        for i in range(len(encrypt)):
            k = encrypt[i]
            temp = []
            for j in range(self.m):
                if mochinver[j] <= k:
                    k = k - mochinver[j]
                    temp.append(1)
                else:
                    temp.append(0)
            result.append(temp)

        return result

    def repart(self, partitions):
        result = []
        for i in range(len(partitions)):
            k = partitions[i]
            temp = self.messagePartitions(k, 1)
            result.append(temp)
        return result

    def encrypt(self, message):
        encrypt = []
        menplabin = self.messagetobin(message)
        mennopart = self.messagebinunion(menplabin)
        mpart = self.messagePartitions(mennopart, self.m)
        m = self.repart(mpart)
        self.s = self.getPublicKey()

        for i in range(0, len(m)):
            item = m[i]
            s = 0
            for j in range(0, len(self.s)):
                s = s + (self.s[j] * int(item[j]))
            encrypt.append(s)

        return encrypt

    def decrypt(self, encrypt):
        M = ""
        ME = []
        MBin = []
        pk = self.getPrivateKey()
        for i in range(0, len(encrypt)):
            ME.append((pk[1] * encrypt[i]) % pk[0])
        print(ME)
        MBin = self.codetobinpartic(ME)
        MDec = self.tobase10(MBin)
        M = self.toChara(MDec)

        return M

    def shammirzippel(self, S, mu):
        CM = []
        PK = []
        q = (S[0] * teoria_numeros.inv(S[1], mu)) % mu
        for i in range(1, (2 ** (len(S) + 1))):
            CM.append(int((i * q) % mu))
        print("CM = ")
        print(CM)
        PK.append(min(CM))
        print(("S'1 = " + str(PK[0])))
        w = int((S[0] * teoria_numeros.inv(PK[0], mu)) % mu)
        print(("w = " + str(w)))
        winv = int(teoria_numeros.inv(w, mu))
        print(("w^-1 = " + str(winv)))
        for i in range(1, len(S)):
            PK.append(int((S[i] * winv) % mu))

        return PK