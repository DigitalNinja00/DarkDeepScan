import sys
import time
import socket


def get_host(direccion):
	try:
		more = socket.gethostbyaddr(direccion)
		print("Hostname : {}".format(more[0]))
	except OSError:
		print("Hostname error")

get_host(sys.argv[1])
user = sys.argv[2].split(None, 10)
lister = list(map(int, user))
for port in lister:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	val = sock.connect_ex((sys.argv[1], port))
	if val==0:
		print("port open {}".format(port))
	else:
		print("Port close {}".format(port))
