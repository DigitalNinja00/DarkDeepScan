import sys
import time
import socket


class dir:
	def gethost(address):
		try:
			more = socket.gethostbyaddr(direccion)
			print("hostname {}".format(more[0]))
		except OSError:
			print("Hostname error")

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
			print("Port scan error")
dir.gethost(sys.argv[1])
Principal.funtion_main_scan()
print("DDS--Basic Scan finished (10.000 ports scanned)")
