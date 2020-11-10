
from flask import Flask , render_template,url_for,jsonify,request
from Usuarios import Usuario
from Recetas import Receta
from Comentarios import Comentario



app = Flask(__name__)
arreglo=[]
cont=0
arreglo.append(Usuario('Usuario','Maestro','admin','admin','administrador'))

listaRecesta=[]
listaRecesta.append(Receta(cont,'David','Pepian','El pepián es un platillo tradicional guatemalteco de origen kaqchiquel propio del departamento de Chimaltenango. Su origen es prehispánico y se servía en las ceremonias religiosas mayas','2 lb. de carne al gusto <br> <br> 1 chile guaque seco <br> <br>  2 onzas de ajonjolí ','Primero, para el Pepián Negro, colocar en una olla la carne a cocer dentro del litro del agua.<br><br>Antes de que esté en su punto, agregar las verduras para su cocimiento.<br><br>Entonces, aparte en un comal, poner a dorar los chiles, el miltomate, el tomate, la cebolla, el ajonjolí, pepitoria, los dientes de ajo, la rajita de canela y la cáscara de plátano.<br><br>Después de que todos los ingredientes se hayan dorado perfectamente, licuar con un poco del caldo donde se ha cocido la carne.','30 minutos','https://www.spanishacademyantiguena.com/assets/design/blogs/level5/pepian-guatemala-recipe-01.jpg'))

listaComentrios=[]
listaComentrios.append(Comentario('0','David_ljr ','03/11/2020      20:00 ','Me gusto la receta '))


@app.route('/', methods=['GET'] )
def inicio():
    return render_template('principalNoRegistrado.html')

@app.route('/inicio', methods=['GET'] )
def rutaLogin():
    return render_template('inicio.html')

@app.route('/cargarRecetas', methods=['GET'] )
def rutaCargarRecetas():
    return render_template('cargarRecetas.html')

@app.route('/modificarRecetas', methods=['GET'] )
def rutaModificarReceta():
    return render_template('modificarReceta.html')

@app.route('/admin', methods=['GET'] )
def rutaadmin():
    return render_template('admin.html')

@app.route('/modificar', methods=['GET'] )
def rutaModificar():
    return render_template('modificar.html')

@app.route('/RecetasPublicadas', methods=['GET'] )
def rutaRecetasPublicadas():
    return render_template('RecetasPublicadas2.html')

@app.route('/RecetaSeleccionada', methods=['GET'] )
def rutaRecetaSeleccionada():
    return render_template('RecetaSelecionada.html')

@app.route('/Cliente', methods=['GET'] )
def rutaCliente():
    return render_template('principalCliente.html')

@app.route('/SeleccionNoCliente', methods=['GET'] )
def rutaNocliente():
    return render_template('RecetaSelecionadaNoCliente.html')   

@app.route('/Perfil', methods=['GET'] )
def rutaPerfil():

    return render_template('modificar.html')

@app.route('/SeleccionCliente', methods=['GET'] )
def rutaSeleccionCliente():

    return render_template('RecetaSelecionadaCliente.html')

@app.route('/NoRegistrado', methods=['GET'] )
def rutaNoregistrado():

    return render_template('principalNoRegistrado.html')


@app.route('/Login', methods=['POST'] )
def Login():
    global arreglo
    username=request.json['usuario']
    pasword=request.json['pasword']
    for usuario in arreglo:
        if usuario.getUsuario()==username and usuario.getPasword()==pasword:
             if usuario.tipo=='administrador':
                 Dato={
                'message':'Admin',
                'usuario':usuario.getUsuario()
                 
                }
                 break
             else:
                 Dato={
                'message':'Success',
                'usuario':usuario.getUsuario()
                 
                }
                 break


        else:
            Dato={
                'message':'Failed',
                'usuario':''
                }
    respuesta=jsonify(Dato)
    return respuesta

@app.route('/Registro', methods=['GET'] )
def rutaRegistro():
    return render_template('registro.html')

@app.route('/portafolio', methods=['GET'] )
def rutaRpo():
    return render_template('portafolio.html')

@app.route('/Personas', methods=['POST'] )
def agregarUsuarios():
     global arreglo
     nombre=request.json['nombre']
     apellido=request.json['apellido']
     username=request.json['usuario']
     pasword=request.json['pasword']
     pasword2=request.json['pasword2']
     tipo=request.json['cliente']
     encontrado=False
     if pasword==pasword2:
         for usuario in arreglo:
             if usuario.getUsuario()==username:
                 encontrado=True
                 break
         if encontrado:
             return jsonify({
                  'message':'Failed',
                  'reason':'Usuario ya registrado'
                  }) 
         else:
              nuevo=Usuario(nombre,apellido,username,pasword,tipo)
              arreglo.append(nuevo)
              return jsonify({
                  'message':'Success',
                  'reason':'Usuario agregado'
                   }) 
         return 'registro exitoso'

     else:
         return jsonify({
                  'message':'Failed2',
                  'reason':'Password no coiciden'
                  }) 

@app.route('/Recetas1', methods=['POST'] )
def agregarRecetas():
     global cont
     cont=cont+1
     
     global listaRecesta
     autor=request.json['autor']
     titulo=request.json['titulo']
     resumen=request.json['resumen']
     ingredientes=request.json['ingredientes']
     preparacion=request.json['preparacion']
     tiempo=request.json['tiempo']
     imagen=request.json['imagen']
     nuevo=Receta(cont,autor,titulo,resumen,ingredientes,preparacion,tiempo,imagen)
     listaRecesta.append(nuevo)
     return jsonify({
         'message':'Success',
         'reason':'Receta agregada'
         }) 
    # return 'registro exitoso'

@app.route('/Comentarios', methods=['POST'] )
def agregarComentarios():
     global listaComentrios
     ids=request.json['ids']
     nombreus=request.json['usuario']
     escrito=request.json['escrito']
     fecha=request.json['fecha']
     nuevo=Comentario(ids,nombreus,escrito,fecha)
     listaComentrios.append(nuevo)
     return jsonify({
         'message':'Success',
         'reason':'comentario agregada'
         }) 
    # return 'registro exitoso'



@app.route('/Personas', methods=['GET'] )
def MostrarUsuarios():
    lista=[]
    global arreglo
    for usuario in arreglo:
        aux= { 
           'nombre':usuario.getNombre(),
           'apellido':usuario.getApellido(),
           'usuario':usuario.getUsuario(),
           'pasword':usuario.getPasword(),
           'tipo':usuario.getTipo()
            }
        lista.append(aux)

    respuesta=jsonify(lista)
    return (respuesta)

@app.route('/Recetas', methods=['GET'] )
def MostrarRecetas():
    lista=[]
    global listaRecesta
    for receta in listaRecesta:
        aux= { 
           'ids':receta.getId(),
           'autor':receta.getAutor(),
           'titulo':receta.getTitulo(),
           'resumen':receta.getResumen(),
           'ingredientes':receta.getIngredientes(),
           'preparacion':receta.getPreparacion(),
           'tiempo':receta.getTiempo(),
           'imagen':receta.getImagen()
            }
        lista.append(aux)

    respuesta=jsonify(lista)
    return (respuesta)

@app.route('/Comentarios', methods=['GET'] )
def MostrarComentarios():
    lista=[]
    global listaComentrios
    for comentarios in listaComentrios:
        aux= { 
           'ids':comentarios.getId(),
           'usuario':comentarios.getNombreU(),
           'escrito':comentarios.getEscrito(),
           'fecha':comentarios.getFecha()
           
            }
        lista.append(aux)

    respuesta=jsonify(lista)
    return (respuesta)


@app.route('/Personas/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre):
    global arreglo
    for usuario in arreglo:
        if usuario.getUsuario() == nombre:
            aux= { 
                'nombre':usuario.getNombre(),
                'apellido':usuario.getApellido(),
                'usuario':usuario.getUsuario(),
                'pasword':usuario.getPasword(),
                'tipo':usuario.getTipo()
                 }
            break
    respuesta = jsonify(aux)
    return(respuesta)

@app.route('/Recetas/<string:nombre>', methods=['GET'])
def ObtenerRecetas(nombre):
    global listaRecesta
    for receta in listaRecesta:
        if receta.getTitulo() == nombre:
            aux= { 
                'ids':receta.getId(),
                'autor':receta.getAutor(),
                'titulo':receta.getTitulo(),
                'resumen':receta.getResumen(),
                'ingredientes':receta.getIngredientes(),
                'preparacion':receta.getPreparacion(),
                'tiempo':receta.getTiempo(),
                'imagen':receta.getImagen()
                 }
            break
    respuesta = jsonify(aux)
    return(respuesta)


@app.route('/Personas/<string:nombre>', methods=['PUT'])

def ActualizarPersona(nombre):
    global arreglo
    encontra=False
    if request.json['estado']=='1':
        for i in range(len(arreglo)):
             if request.json['usuario'] == arreglo[i].getUsuario():
                 encontra=True
                 break    
        if encontra:
            return jsonify({
                  'message':'Existe',
                  'reason':'Usuario ya registrado'
                  }) 
        else:
            for i in range(len(arreglo)):
                if nombre == arreglo[i].getUsuario():
                    arreglo[i].setNombre(request.json['nombre'])
                    arreglo[i].setApellido(request.json['apellido'])
                    arreglo[i].setUsuario(request.json['usuario'])
                    arreglo[i].setPasword(request.json['pasword'])
                    arreglo[i].setTipo(request.json['tipo'])
                    break

        
    else:                      
        for i in range(len(arreglo)):
            if nombre == arreglo[i].getUsuario():
                arreglo[i].setNombre(request.json['nombre'])
                arreglo[i].setApellido(request.json['apellido'])
                arreglo[i].setUsuario(request.json['usuario'])
                arreglo[i].setPasword(request.json['pasword'])
                arreglo[i].setTipo(request.json['tipo'])
                break

    return jsonify({'message':'Se actualizo el dato exitosamente'})

@app.route('/Recetas/<string:nombre>', methods=['PUT'])
def ActualizarRecetas(nombre):
    global listaRecesta
    
    for i in range(len(listaRecesta)):
        if nombre == listaRecesta[i].getTitulo():
            listaRecesta[i].setAutor(request.json['autor'])
            listaRecesta[i].setTitulo(request.json['titulo'])
            listaRecesta[i].setResumen(request.json['resumen'])
            listaRecesta[i].setIngredientes(request.json['ingredientes'])
            listaRecesta[i].setPreparacion(request.json['preparacion'])
            listaRecesta[i].setTiempo(request.json['tiempo'])
            listaRecesta[i].setImagen(request.json['imagen'])
            break
        

    return jsonify({'message':'Se actualizo el dato exitosamente' })

@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global arreglo
    for i in range(len(arreglo)):
        if nombre == arreglo[i].getUsuario():
            del arreglo[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})

@app.route('/Recetas/<string:nombre>', methods=['DELETE'])
def EliminarRecetas(nombre):
    global listaRecesta
    for i in range(len(listaRecesta)):
        if nombre == listaRecesta[i].getTitulo():
            del listaRecesta[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})





if __name__ == "__main__":
    app.run( debug=True)