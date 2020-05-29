import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'admin1' 
DB_NAME = 'sakila' 

print(DB_HOST, DB_USER, DB_PASS, DB_NAME)

miConexion = MySQLdb.connect( DB_HOST, DB_USER, DB_PASS, DB_NAME )
cur = miConexion.cursor()
cur.execute( "SELECT crm_info_id FROM crm_information limit 10" )
for crm_info_id in cur.fetchall() :
    print (crm_info_id)
miConexion.close()

print ("Consulta")

try:
    def run_query(query=''): 
        print("hola2")
        datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
        
        conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
        print(conn)
        cursor = conn.cursor()         # Crear un cursor 
        cursor.execute(query)          # Ejecutar una consulta 

        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()   # Traer los resultados de un select 
        else: 
            conn.commit()              # Hacer efectiva la escritura de datos 
            data = None 
        
        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 

        return data
except:
     print ("no funciona")
    
print(run_query("SELECT crm_info_id FROM crm_information limit 2"))