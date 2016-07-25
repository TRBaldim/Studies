
class V:
    def __init__(self, obj):
        self.obj = obj
        self.edges = []
        self.dephs = 0
    def setEdge(self, e):
        self.edges.append(e)
    def __str__(self):
        retorno = ""
        self.dephs += 1
        if self.dephs > 1:
            return str(self.obj) + ' ... '
        if self.edges == []:
            return str(self.obj)
        else:
            for i in self.edges:
                retorno += str(str(self.obj)  + str(i) + " :> " + str(i.point)) + ' '
                retorno += '\n'
                #self.dephs = 0
                #print retorno
        return retorno

class E:
    def __init__(self, obj, v1, v2, name):
        self.obj = obj
        self.name = str(name)
        self.point = v2
        v1.setEdge(self)
    def __str__(self):
        return " :> " + str(self.name) + ">" + str(self.obj) 
    

if __name__ == '__main__':
    a1 = V('EU')
    a2 = V('VC')
    a3 = V('ELA')
    a4 = V('OUTRO')
    a5 = V('KK')
    a6 = V('NNK')
    a7 = V('JJ')
    E(10, a1, a2, 'R')
    E(5, a2, a3, 'R')
    E(11, a3, a1, 'R')
    E(1, a1, a4, 'R')
    E(2, a5, a2, 'R')
    E(2, a1, a6, 'R')
    E(1, a2, a4, 'R')
    E(99, a5, a2, 'R')
    E(5, a6, a7, 'R')
    E(9, a7, a5, 'R')
    print (a1)
