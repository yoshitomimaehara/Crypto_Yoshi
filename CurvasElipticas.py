import teoria_numeros


class CurvasElipticas:

    def __init__(self):
        self.lamda = 0
        self.a = 1
        self.b = 1

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def calculateLambda(self, P, Q, n):
        if P[0] != Q[0]:
            calc = teoria_numeros.inv((P[0] - Q[0]), n)
            self.lamda = ((P[1] - Q[1]) * calc) % n
        elif P[0] == Q[0]:
            calc = (3 * teoria_numeros.exponenciacion(P[0], 2, n) + self.a) % n
            self.lamda = calc * teoria_numeros.inv((2 * P[1]), n)

    def suma(self, P, Q, n):
        result = []
        if self.lamda == 0:
            self.calculateLambda(P, Q, n)

        x3 = (teoria_numeros.exponenciacion(self.lamda, 2, n) - P[0] - Q[0])
        y3 = ((P[0] - x3) * self.lamda - P[1])

        while x3 < 0:
            x3 = x3 + n

        while x3 > n:
            x3 = x3 - n

        while y3 < 0:
            y3 = y3 + n

        while y3 > n:
            y3 = y3 - n

        result.append(x3)
        result.append(y3)
        return result

    def multiplicacion(self, k, P, n):
        temp = []
        if k > 0:
            PT = P
            for i in range(1, k):
                temp = self.suma(PT, P, n)
                PT.clear()
                PT.append(temp[0])
                PT.append(temp[1])
        elif k < 0:
            PT = P * (-1)
            for i in range(1, k):
                temp = self.suma(PT, (P * (-1)), n)
                PT.clear()
                PT.append(temp[0])
                PT.append(temp[1])
        else:
            print("Punto en el Infinito")
        return PT

    def generateTabla(self, n):
        table = []
        temp = []
        for i in range(0, n):
            z = ((i) ** 3 + self.a * i + self.b) % n

            if teoria_numeros.jacobi(z, n) == 1:
                res = "SI"
            else:
                res = "NO"

            if res == "SI":
                #y1 = teoria_numeros.exponenciacion(z, ((n + 1) / 4), n)
                #y2 = n - y1
                #y12 = [y1, y2]
                y12 = teoria_numeros.raizcuadradaprima(z, 11)
            else:
                y12 = []

            temp = [i, z, res, y12]
            table.append(temp)

        return table

    def constructTable(self, n):
        table = cv.generateTabla(n)
        print(["i", "z", "res", "y12"])
        for i in range(len(table)):
            print((table[i]))


if __name__ == "__main__":
    cv = CurvasElipticas()
    #cv.setA(3)
    #cv.setB(6)
    #cv.calculateLambda([10, 7], [1, 4], 13)
    #print((cv.lamda))
    #print((cv.suma([0, 1], [1, 4], 13)))
    #print((cv.multiplicacion(21, [0, 1], 79)))
    #H = cv.multiplicacion(2, [1, 4], 13)
    #H = cv.multiplicacion(2, [0, 1], 13)
    #K = cv.suma(H, [1, 4], 13)
    #print(K)
    #print((cv.suma(H, [0, 1], 13)))
    #print((cv.construirTabla(11)))
    #cv.constructTable(11)
