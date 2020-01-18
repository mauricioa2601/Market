from clases.conexion import Conexion
class detalleProducto():
    def __init__(self):
        self.conexion = Conexion()
        
    def listar(self,id):
    query = 'SELECT * FROM boletas b inner join productos p on b.idcliente = c.idcliente and fecha between'
     ##FALTA 
    resultado = self.conexion.ejecutarQuery(query)
    filas = resultado.fetchall()
    print(filas)    
        
        