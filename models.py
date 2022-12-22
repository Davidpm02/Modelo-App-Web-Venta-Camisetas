from db import Base
from flask_login import UserMixin

from sqlalchemy import Column, Integer, String, Boolean, VARCHAR


from werkzeug.security import generate_password_hash, check_password_hash


class Productos(Base):
    __tablename__ = 'producto'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)  # Este valor no lo vamos a inicializar nosotros.Se creara de
    # manera automatica al crear cada objeto.
    nombre = Column(String(200), nullable=False)  # El parametro 'nullable' hace que la columna 'nombre'
    # de la tabla nunca pueda estar vacia o recibir como dato un None.
    stock = Column(Integer, nullable = False)
    talla = Column(VARCHAR(50), nullable = False)
    def __init__(self,nombre,stock,talla):
        self.nombre = nombre
        self.stock = stock
        self.talla = talla
        

        
            
    def __str__(self):
        return " {} --> {} --> {} ".format(self.id,
                                           self.nombre,
                                           self.stock)        