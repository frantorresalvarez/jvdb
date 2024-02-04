import subprocess


operacion = "insert"
basededatos = "miempresa"
coleccion = "clientes"
documento = "cliente8"
contenido = "este es otro contenido de prueba"

comando = '"C:\\Users\\franc\\Documents\\GitHub\\jvdb\\jvdb.exe" '+operacion+' '+basededatos+' '+coleccion+' '+documento+' "'+contenido+'"'
resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)


if resultado.returncode == 0:
    print("ok")
else:
    print("ko")
