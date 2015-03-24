import httplib,urllib
import re, urllib2
import random
from random import choice

# VARIABLES
#--------------------------------------------------------------#
RutaCCcam = 'XGV0Y1xDQ2NhbS5jZmc='.decode('base64','strict')
RutaCCcam = 'QzpcXFVzZXJzXFxLXFxEZXNrdG9wXFxDQ2NhbS5jZmc='.decode('base64','strict')
#--------------------------------------------------------------#

# FUNCIONES
#--------------------------------------------------------------#
def BorrarLineasAntiguas():
	'''Borra todas las lineas del .cfg CCcam dejando solo la primera si la hubiese'''
	global RutaCCcam
	lineas=""
	# leemos posibles lineas previas
	try:
		archi = open(RutaCCcam,'r')
		lineas = archi.readlines()
		archi.close()
	except:
		pass
	# mantenemos una linea para que no haga paron de imagen (smooth line update)
	archi = open(RutaCCcam,'w')
	for linea in reversed(lineas):
		if linea.find('C:') == 0:
			archi.write(linea)
			break
	

def escribirLineaenCCcam(linea):
	'''Escribe la linea pasada por parametro a la funcion en el .cfg CCcam'''
	global RutaCCcam
	archi = open(RutaCCcam,'a+')
	archi.write(linea + "\n")
	archi.close()
	
	
def sacarTipo1(url):
	h = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"}
	cookie_h = urllib2.HTTPCookieProcessor()
	opener = urllib2.build_opener(cookie_h)
	urllib2.install_opener(opener)
	f = urllib2.urlopen(url)
	html = f.read()
	html_oneline = html.replace("\n","")
	lineare = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*?)',html_oneline)
	if lineare:
		LINEA = "C: " + lineare.group(2) + " " +  lineare.group(3) + " " + lineare.group(4) + " " + lineare.group(5)
		return LINEA
	else:
		return "# " + url + " no produjo linea"

	
	
def sacarTipo2(url):
	'''Scraping a hack-sat para obtener la linea que nos genera'''
	connection = httplib.HTTPConnection(url)
	parametros = urllib.urlencode({"user":"84.194."+str(random.randrange(0,255))+"."+str(random.randrange(0,255)),"pass":"hack-sat.com","submit":"Activate%21"})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	connection.request("POST", "/h25/index.php", parametros, headers)
	response = connection.getresponse()
	html = response.read()
	html_oneline = html.replace("\n","")
	lineare = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*?)',html_oneline)
	if lineare:
		LINEA = "C: " + lineare.group(2) + " " +  lineare.group(3) + " " + lineare.group(4) + " " + lineare.group(5)
		return LINEA
	else:
		return "# " + url + " no produjo linea"


		
def sacarTipo3(url):
	conexion = httplib.HTTPConnection("bypassshorturl.com")
	parametros = urllib.urlencode({"url": url})
	cabezera = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conexion.request("POST", "/get.php", parametros, cabezera)
	respuesta = conexion.getresponse()
	LeerRespuesta = str(respuesta.read())
	LeerRespuesta = LeerRespuesta.replace("http://", "")
	LeerRespuesta = LeerRespuesta.split("/")

	url_bypass = LeerRespuesta[0]
	
	try:
		pass_bypass = str("/" + LeerRespuesta[1] + "/" + LeerRespuesta[2])
	except:
		pass_bypass = str("/" + LeerRespuesta[1])
		
	rand_valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pass_longitud = 10
	PASS = "".join([choice(rand_valores) for i in range(pass_longitud)])
	connection = httplib.HTTPConnection(url_bypass)
	parametros = urllib.urlencode({"user":"84.194."+str(random.randrange(0,255))+"."+str(random.randrange(0,255)),"pass":PASS})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	connection.request("POST", pass_bypass, parametros, headers)
	response = connection.getresponse()
	html = response.read()
	connection.close()
	html_oneline = html.replace("\n","")
	lineare = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*?)',html_oneline)
	if lineare:
		LINEA = "C: " + lineare.group(2) + " " +  lineare.group(3) + " " + lineare.group(4) + " " + lineare.group(5)
		return LINEA
	else:
		return "# " + url + " no produjo linea"


def sacarTipo4(url):
	rand_valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pass_longitud = 10
	PASS = "".join([choice(rand_valores) for i in range(pass_longitud)])
	connection = httplib.HTTPConnection(url)
	parametros = urllib.urlencode({"Username":PASS,"cline":""})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	connection.request("POST", "/index.php", parametros, headers)
	response = connection.getresponse()
	html = response.read()
	connection.close()
	html_oneline = html.replace("\n","")
	lineare = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*?)',html_oneline)
	if lineare:
		LINEA = "C: " + lineare.group(2) + " " +  lineare.group(3) + " " + lineare.group(4) + " " + lineare.group(5)
		return LINEA
	else:
		return "# " + url + " no produjo linea"

# TO-DO: anadir el bypasser a esta url
def sacarTipo5(url):
	'''Scraping a dz-sat zapto para obtener la linea que nos genera'''
	rand_valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pass_longitud = 10
	PASS = "".join([choice(rand_valores) for i in range(pass_longitud)])
	connection = httplib.HTTPConnection(url)
	parametros = urllib.urlencode({"user":"84194"+str(random.randrange(0,255))+str(random.randrange(0,255)),"pass":PASS})
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"}
	connection.request("POST", "/generator/index.php", parametros, headers)
	response = connection.getresponse()
	html = response.read()
	# print(html)
	html_oneline = html.replace("\n","")
	lineare = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*?)',html_oneline)
	if lineare:
		LINEA = "C: " + lineare.group(2) + " " +  lineare.group(3) + " " + lineare.group(4) + " " + lineare.group(5)
		return LINEA
	else:
		return "# " + url + " no produjo linea"
		

	
#--------------------------------------------------------------#
# MAIN
#--------------------------------------------------------------#

#Borrar Lineas anteriores
BorrarLineasAntiguas()

linea = sacarTipo1("687474703a2f2f647265616d2d7365647563742e6f72672f73312e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f647265616d2d7365647563742e6f72672f73322e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f647265616d2d7365647563742e6f72672f73332e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f647265616d2d7365647563742e6f72672f73342e706870".decode("hex"))
escribirLineaenCCcam(linea)

linea = sacarTipo1("687474703a2f2f7777772e6d79636363616d32342e636f6d2f66617374312e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f7777772e6d79636363616d32342e636f6d2f66617374322e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f7777772e6d79636363616d32342e636f6d2f66617374332e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f7777772e6d79636363616d32342e636f6d2f66617374342e706870".decode("hex"))
escribirLineaenCCcam(linea)

linea = sacarTipo1("687474703a2f2f6d68726163682e7a6170746f2e6f72672f636363616d2f737672312e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f6d68726163682e7a6170746f2e6f72672f636363616d2f737672322e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f6d68726163682e7a6170746f2e6f72672f636363616d2f737672332e706870".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo1("687474703a2f2f6d68726163682e7a6170746f2e6f72672f636363616d2f737672342e706870".decode("hex"))
escribirLineaenCCcam(linea)


linea = sacarTipo2("6b616465722d7361742e64646e732e6e6574".decode("hex"))
escribirLineaenCCcam(linea)
linea = sacarTipo2("6861636b7361742e64646e732e6e6574".decode("hex"))
escribirLineaenCCcam(linea)

linea = sacarTipo3("687474703a2f2f6164662e6c792f7664596554".decode("hex"))
escribirLineaenCCcam(linea)

linea = sacarTipo3("687474703a2f2f6164662e6c792f764636675a".decode("hex"))
escribirLineaenCCcam(linea)

linea = sacarTipo4("647265616d34657665722e696e666f".decode("hex"))
escribirLineaenCCcam(linea)

'''
linea = sacarTipo5("647a2d7361742e7a6170746f2e6f7267")
escribirLineaenCCcam(linea)
'''
