# Ejemplo de implementacion ZODB

# creado por Dominguez Contreras (Sala 5)
# Muestra la diferencia entre la base de datos en memoria y persistente

# Se debe ejecutar 2 veces seguidas para visualizar los conceptos

from account import Account
from connection import Connection
import transaction

#creamos el objeto que deseamos guardar
cuenta = Account('Pablo')
cuenta.deposit(20)
cuenta.deposit(40.2)

#usamos nuestro objeto conexion para guardar los datos
db = Connection()
root = db.getRoot()

print("Base de datos inicial:")

#revisamos si la base de datos esta creada
if "accounts" not in root:
    root['accounts'] = {} #sino lo esta la generamos t.q: root.noombreDeLaBD
    print("\tVacia")

accounts = root['accounts'] #la variable accounts ahora contiene nuestra BD

#imprimimos los valores de nuestra BD si es que existen
for elem in accounts.values():
    print(elem.owner,"tiene",elem.balance)

#revisamos si la llave que identifica a la cuenta de Pablo existe en la BD
#en la primera ejecucion de este script no existirá
if 'Pablo' not in accounts:
    print("\t la cuenta de pablo ha sido creada")
    accounts['Pablo'] = cuenta #Agregamos la cuenta de pablo a la BD
    transaction.commit() # guardamos los datos en la BD persistente
else:
    # este msj es arrojado en la 2da ejecucion gracias a que 
    # hicimos commit en la primera ejecucion
    print("\t la cuenta de pablo ya no fue agregada")    

db.close() #cerramos la BD

root = db.getRoot() #volvemos a abrir la BD
accounts = root['accounts']

#despues de cerrar la base de datos revisamos que los cambios persisten
for elem in accounts.values():
    print(elem.owner,"tiene",elem.balance)

# ahora creamos una nueva cuenta para mostrar que sino se hace commit
# la base de datos solo se actualiza en caché
cuenta1 = Account('Juan')
cuenta1.deposit(10)
accounts['Juan'] = cuenta1
root['accounts'] = accounts
root['accounts']['Juan'].cash(5) #otra forma de acceder al objeto una vez que esta en la BD
transaction.commit() #<------- si esta linea no existe los datos solo se guardan en cache y al terminar la ejecucion del programa no persisten
accounts['Pablo'].cash(20) # modificamos tambien el objeto que ya habiamos guardado

print("Cuentas actualizadas:")
for elem in root['accounts'].values():
    print(elem.owner,"tiene",elem.balance)

#podemos revertir los cambios que van a persistir con
#transaction.abort()
#hacemos nuevo cambios
#accounts['Pablo'].cash(20)
#transaction.commit()

