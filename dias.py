import os
import sys
import time


def semana():
	print "           "
	print "           "
	print "           "
	print "                                      >>>>>DIAS DE LA SEMANA<<<<<<"
	print "                                           -----------"
	print "                        "
	print "     1 DOMINGO."
	print "           "
	print "     2 LUNES."
	print "            "
	print "     3 MARTES."
	print "            "
	print "     4 MIERCOLES."
	print "            "
	print "     5 JUEVES."
	print "            "
	print "     6 VIERNES."
	print "              "
	print "     7 SABADO."
	Numero = raw_input("ingrese el numero: ")

	if Numero.isalpha() == True:
		print "            "
		print "               NO SE PERMITEN LETRAS"
		time.sleep(2)
		os.system("cls")

	else:
		if Numero =="1":
			print "                     DOMINGO"
		elif Numero =="2":
			print "                     LUNES"
		elif Numero =="3":
			print "                     MARTES"
		elif Numero =="4":
			print "                     MIERCOLES"
		elif Numero =="5":
			print "                     JUEVES"
		elif Numero == "6":
			print "                     VIERNES"
		elif Numero == "7":
			print "                     SABADO"
		else:
			print "Numero Erroneo"
			time.sleep(1)
			os.system("cls")
				

def ecuacion():
		print ("M = 6 * L / 2")
		L = input("ingrese la variable L: ")
		M = 6 * L / 2
		print ("El resultado de M es: "+str(M))

def menuprincipal():
	print " 1 semana"
	print " 2 ecuacion"
	Numero = raw_input("ingrese opcion: ")

	if Numero == "1":
		print "A elegido la semana"
		semana()
	elif Numero == "2":
		print "A elegido la ecuacion"
		ecuacion()
	else:
		print "Numero Erroneo"
		time.sleep(1)
		os.system("cls")
		menuprincipal()

menuprincipal()