#file_a = "alfabeto.alf"
file_a = "ascii.alf"


def getAlpha():
        alpha = {}
        f = open(file_a, "r")
        temp1 = f.readline()
        while temp1:
            temp = temp1.split(" => ")
            temp1 = f.readline()
            alpha[temp[0]] = temp[1].rstrip("\n")
        f.close()
        return alpha


def getFirstkeyAlpha():
        alpha = list(getAlpha().keys())
        return alpha[0]


def getLenghtalphaKey():
        alpha = getAlpha()
        return len(alpha[getFirstkeyAlpha()])


def toDigits(partitions, r):
        result = []
        temp = ""
        j = 0
        alfabeto = getAlpha()
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


def toChara(partitions):
        result = ""
        keys = []
        alfabeto = getAlpha()
        keys = sorted(alfabeto.keys())
        for i in range(0, len(partitions)):
            for j in range(0, len(keys)):
                if alfabeto.get(keys[j]) == partitions[i]:
                    result = result + keys[j]

        return result