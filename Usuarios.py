class Usuario:
    def __init__(self,nombre,apellido,usuario,pasword,tipo):
        self.nombre=nombre
        self.apellido=apellido
        self.usuario=usuario
        self.pasword=pasword
        self.tipo=tipo
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUsuario(self):
        return self.usuario

    def getPasword(self):
        return self.pasword
    
    def getTipo(self):
        return self.tipo
    
    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setApellido(self,apellido):
        self.apellido=apellido
    
    def setUsuario(self,usuario):
        self.usuario=usuario

    def setPasword(self,pasword):
        self.pasword=pasword
    
    def setTipo(self,tipo):
        self.tipo=tipo
    




    
    

