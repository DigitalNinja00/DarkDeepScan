import sys
import time
import socket


class Pendejada:
	def gethost(direccion):
		try:
			more = socket.gethostbyaddr(direccion)
			print("Nombre del host {}".format(more[0]))
		except OSError:
			print("Error al obtener el nombre del host")

class Principal:
	def funtion_main_scan():
		try:
			host = sys.argv[1]
			for port in range(10000):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				value = sock.connect_ex( (host, port) )
				if value==0:
					print("port open {}".format(port))
				else:
					pass
		except OSError:
			print("Error al realizar el escaneo de puertos")
Pendejada.gethost(sys.argv[1])
Principal.funtion_main_scan()
print("DDS--Escaneo bAsico Finalizado (10.000 puertos escaneados)")