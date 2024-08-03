# Diccionarios
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

import pandas as pd

class ProductosControler:
    '''Clase que recibe un conjunto de diccionarios y controla los métodos
    Agregar , Eliminar , Actualizar y Salir
    '''
    def __init__(self,Productos,Precios,Stock):
        self.Productos = Productos
        self.Precios = Precios
        self.Stock = Stock
        self.cantidad_total = len(self.Productos)
        self.Producto_Table = self.generate_dataframe()
        self.Salir = False

    def generate_dataframe(self):
        ''' Funcion que genera un dataframe con los diccionarios'''
        dic = {
            'Nombre': self.Productos.values() ,
            'Precio': self.Precios.values() ,
            'Cantidad': self.Stock.values()
        }
        return pd.DataFrame(dic,index = range(1,self.cantidad_total + 1))

    def mostrar_prod(self):
        print('\n--------------------------------------------------')
        print('\t[+] Productos')
        print('--------------------------------------------------')
        print(self.Producto_Table)
        
    def mostrar_op(self):
        print('\n[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir ')        
        self.input = int(input('Elija una opcion:'))
        print()
        
    def run(self):
        
        while(self.Salir==False):
            
            self.mostrar_prod()
            self.mostrar_op()
            
            if(self.input==1):
                try:
                    nombre = input('Ingresa el nombre del Producto: ')
                    precio = float(input('Ingresa el precio total: '))
                    cantidad  = int(input('Ingresa la cantidad : '))
                    registro = {'Nombre': nombre, 'Precio': precio, 'Cantidad': cantidad}
                    self.agregar(registro)
                except:
                    print('Ingreso de datos incorrectos.')
                
            elif self.input==2:
                indice = int(input('Ingresa el indice del registro a eliminar'))
                self.eliminar(indice)
            elif self.input==3:
                self.actualizar()
            elif self.input==4:
                print('Programa Finalizado')
                self.salir()
            else:
                print('Ingresar un valor entre [1-4]')               
    
   
    def agregar(self,registro):
        self.Producto_Table.loc[self.cantidad_total+1] = registro.values()
        self.cantidad_total+=1
        
    def eliminar(self,indice):
        try:
            self.Producto_Table = self.Producto_Table.drop(indice)
            self.Producto_Table.index = range(1, self.cantidad_total)
            self.cantidad_total-=1
        except:
            print(f'No existe el indice: {indice}')

    def actualizar(self):
        try:
            indice = int(input('Ingresa el índice del registro a actualizar: '))
            if indice not in self.Producto_Table.index:
                raise KeyError
            nombre = input('Ingresa el nuevo nombre del Producto: ')
            precio = float(input('Ingresa el nuevo precio: '))
            cantidad = int(input('Ingresa la nueva cantidad: '))
            self.Producto_Table.at[indice, 'Nombre'] = nombre
            self.Producto_Table.at[indice, 'Precio'] = precio
            self.Producto_Table.at[indice, 'Cantidad'] = cantidad
        except KeyError:
            print(f'No existe el índice: {indice}')
        except ValueError:
            print('Entrada no válida. Asegúrese de ingresar los datos correctamente.')
    def salir(self):
        self.Salir=True

p = ProductosControler(Productos,Precios,Stock)
p.run()
