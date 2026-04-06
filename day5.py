

#============================ Matrix
class Graph:
    def __init__(self,size):
        self.size = size
        self.graph = [[0]*size for i in range(size) ]
        self.dic = {"S":0 ,"K":1 ,"P":2 ,"C":3 ,"B":4 ,"R":5 ,"V":6 ,"G":7 }

    def insert(self,s,d):
        row = self.dic[s]
        col = self.dic[d]
        self.graph[row][col] = 1
        self.graph[col][row] = 1

andhra = Graph(8)
datas = [("S","K"),("S","P"),("S","R"),("K","C"),("K","V"),("P","C"),("V","G"),("R","B")]
for s,d in datas:
    andhra.insert(s,d)
for i in range(8):
    print(andhra.graph[i])


#=========================== List


class Graph:
    def __init__(self):
        self.graph = {}

    def insert(self,s,d):
        for i in range(2):
            if s in self.graph:
                self.graph[s].append(d)
            else:
                self.graph[s] = [d]
            s , d = d , s


andhra = Graph()
datas = [("S","K"),("S","P"),("S","R"),("K","C"),("K","V"),("P","C"),("V","G"),("R","B")]
for s,d in datas:
    andhra.insert(s,d)
print(andhra.graph)

