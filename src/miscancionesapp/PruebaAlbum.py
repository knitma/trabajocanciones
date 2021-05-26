from src.miscancionesapp.modelo.cancion import Cancion
from src.miscancionesapp.modelo.interprete import Interprete
from src.miscancionesapp.modelo.album import Album, Medio
from src.miscancionesapp.modelo.declarative_base import Session, engine, Base
from src.miscancionesapp.logica.coleccion import Coleccion

if __name__ == '__main__':
    #Crea la BD
    Base.metadata.create_all(engine)

    #Abre la sesion
    session = Session()
    colecion=Coleccion()

    #USAR LA BD QUE ESTA DENTRO DE LA CARPETA SRC\miscancionesapp

    """if colecion.agregar_album("La incondicional" , 1990 , "Son baladas" , Medio.CD ):
        print("Se añadio con exito")
    else:
        print ( "Ya se encuentra el album" )

    if colecion.editar_album(1,"Romances",1992,"Son baladas",Medio.DISCO):
        print("Se Modifico con exito")

    if colecion.agregar_cancion("Hasta que me olvides" , 2 , 23 , "Armando Manzanero" ):
        print("Se añadio con exito")
    else:
        print ( "Ya se encuentra la cancion" )

    if colecion.editar_cancion(1, "Como te atreves", 2, 25, "Pepe Armando"):
        print("Se Modifico con exito")

    if colecion.agregar_interprete("Luis miguel","La fama subio por su serie", 1):
        print("Se añadio con exito")
    else:
        print("Ya se encuentra el interprete")

    if colecion.editar_interprete(1, "Luis miguel","Cancion dedicada a su ex pareja", 1):
        print("Se Modifico con exito")"""
