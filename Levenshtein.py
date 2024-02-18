class LevBottomUp():
    def __init__(self):
        pass

    def matrix(self, a, b):
        fila = len(b) + 1
        columna = len(a) + 1
        dp = [[0] * columna for _ in range(fila)]

        for i in range(len(a)+1):
            dp[0][i] = i
        for i in range(len(b)+1):
            dp[i][0] = i
        dp[0][0] = 0
        self.bottom_up_operaciones(dp, a, b) #quiete return
        return self.bottom_up(dp, a, b)
    
    def bottom_up(self, dp, a, b):
        for i in range(1, len(b) + 1):
            for j in range(1, len(a) + 1):
                if a[j-1] == b[i-1]:
                    dp[i-1][j-1] = dp[i-1][j-1]
                else: 
                    dp[i-1][j-1] += 1
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])
        return dp[len(b)][len(a)]
    





    def matrix2(self, a, b):
        fila = len(b) + 1
        columna = len(a) + 1
        dp = [[0] * columna for _ in range(fila)]

        for i in range(len(a)+1):
            dp[0][i] = "n"
        for i in range(len(b)+1):
            dp[i][0] = "n"
        dp[0][0] = "n"
        return dp
        #print(dp)
    
    def bottom_up_operaciones(self, dp, a, b):
        ops = self.matrix2(a, b)
        #print(ops)
        for i in range(1, len(b) + 1):
            for j in range(1, len(a) + 1):
                if a[j-1] == b[i-1]:
                    dp[i-1][j-1] = dp[i-1][j-1]
                else: 
                    dp[i-1][j-1] += 1
                if dp[i-1][j] + 1 <= dp[i][j-1] + 1 and dp[i-1][j] + 1 <= dp[i-1][j-1]:
                    dp[i][j] = dp[i-1][j] + 1
                    ops[i][j] = "e"
                elif dp[i][j-1] + 1 <= dp[i-1][j] + 1   and dp[i][j-1] + 1 <= dp[i-1][j-1]:
                    dp[i][j] = dp[i][j-1] + 1
                    ops[i][j] = "a"
                else:
                    if a[j-1] == b[i-1]:
                        ops[i][j] = "n"
                    else: 
                        ops[i][j] = "s"
                    dp[i][j] = dp[i-1][j-1]
                    
        """for i in range(0, len(b) +1 ):
            for j in range(0, len(a)+1):
                print(ops[i][j], end = ' ')
            print()
        print(dp[len(b)][len(a)])"""
        self.pasos(a, b, ops) #quite return 
    
    def pasos(self, a, b, ops):
        i = len(b)
        j = len(a)
        while i >= 1 and j >= 1:
            if ops[i][j] == "e":
                print("Añade", b[i-1])
                i -= 1
            elif ops[i][j] == "a":
                print("Elimina" , a[j-1])
                j -= 1
            elif ops[i][j] == "s":
                print("Sustituye", a[j-1], " por ", b[i-1])
                i -= 1
                j -= 1
            elif ops[i][j] == "n":
                print("Nada")
                i -= 1
                j -= 1

Objeto = LevBottomUp()
print(Objeto.matrix("corazon", "cascara"))
#Objeto.matrix("corazon", "cascara")
