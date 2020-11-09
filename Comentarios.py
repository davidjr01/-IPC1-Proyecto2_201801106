class Comentario:
    def __init__(self,ids ,nombreU, escrito,fecha):
        self.ids=ids
        self.escrito=escrito
        self.fecha=fecha
        self.nombreU=nombreU

    def getId(self):
        return self.ids

    def getNombreU(self):
        return self.nombreU
    
    def getEscrito(self):
        return self.escrito

    def getFecha(self):
        return self.fecha

    def setId(self,ids):
        self.ids=ids
    
    def setNombreU(self,nombreU):
        self.nombreU=nombreU
    
    def setEscrito(self,escrito):
        self.escrito=escrito
    
    def setFecha(self,fecha):
        self.fecha=fecha