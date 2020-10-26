Para correr el proyecto siga los siguientes pasos:

Desde un dispositivo donde esté "git" instalado, abra una consola y digite el siguiente comando: 
    
git clone https://github.com/jsacevedoc/PR-CTICA-TELEMATIX.git

Ejecutar SERVIDOR/server.py 
Ejecutar CLIENTE/client.py (Desde otra consola diferente)

Descripción de comandos:

QUIT: Desconexión desde el cliente al servidor
DATA: Envío de texto simple para ser escritos en un archivo en el servidor
HELO: Prueba de conexión
NBUCK: Crear un nuevo Bucket
DLBUCK: Eliminar un Bucket
UPFILE: Transferir un archivo desde el cliente al servidor
DNFILE: Transferir un archivo desde el servidor al cliente
DLFILE: Eliminar un archivo
LIST: Ver los archivos y buckets en el servidor
CD: Cambiar el workspace a un bucket específico (Navegar entre buckets)
BK: Retroceder el workspace (Retroceder entre buckets)


Nota:
En las pruebas locales que hicimos, creamos un nuevo Bucket llamado "TESTSOCKBUCKET1", posteriormente, transferimos a este bucket el archivo llamado "ClientFile.txt" desde la carpeta "CLIENTE".

Proyecto elaborado por:

Jhonatan Acevedo Castrillón
Juan José Escudero Valencia