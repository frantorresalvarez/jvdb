import subprocess

comando = '"C:\\Users\\franc\\Documents\\GitHub\\jvdb\\jvdb.exe" insert miempresa clientes cliente7 "Este es el cliente7"'
resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)


if resultado.returncode == 0:
    print("ok")
else:
    print("ko")
