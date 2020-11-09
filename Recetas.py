class Receta:
    def __init__(self,ids,autor,titulo,resumen,ingredientes,preparacion,tiempo,imagen):
        self.ids=ids
        self.autor=autor
        self.titulo=titulo
        self.resumen=resumen
        self.ingredientes=ingredientes
        self.preparacion=preparacion
        self.tiempo=tiempo
        self.imagen=imagen  


    def getId(self):
        return self.ids
        
    
    def getAutor(self):
        return self.autor


    def getTitulo(self):
        return self.titulo
    
    def getResumen(self):
        return self.resumen
    
    def getIngredientes(self):
        return self.ingredientes
    
    def getPreparacion(self):
        return self.preparacion
    
    def getTiempo(self):
        return self.tiempo
    
    def getImagen(self):
        return self.imagen
    
    def setId(self,ids):
        self.ids=ids

    def setAutor(self,autor):
        self.autor=autor

    def setTitulo(self,titulo):
        self.titulo=titulo
    
    def setResumen(self,resumen):
        self.resumen=resumen
               
    def setIngredientes(self,ingredientes):
        self.ingredientes=ingredientes

    def setPreparacion(self,preparacion):
        self.preparacion=preparacion

    def setTiempo(self,tiempo):
        self.tiempo=tiempo

    def setImagen(self,imagen):
        self.imagen=imagen
        

        
