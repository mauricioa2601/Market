from clases.conexion import Conexion
class Boletas():
    def __init__(self):
        self.conexion = Conexion()
    
    def listar(self,fecha):
        query = 'SELECT * FROM boletas b inner join clientes c on b.idcliente = c.idcliente and fecha between'  
        resultado = self.conexion.ejecutarQuery(query)
        filas = resultado.fetchall()
        print(filas)
        
        