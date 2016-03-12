print "calculadora"
print "1 suma"
print "2 resta"
print "3 multiplicar"
print "4 dividir"
print "5 potenciacion"
Numero = input("ingrese el numero de la funcion que desea")
if Numero ==1:
	print "puede empesar a sumar"
elif Numero ==2:
	print "puede empesara a restar"
elif Numero ==3:
	print "puede empesar a multiplicar"
elif Numero ==4:
	print "puede empesar a dividir"
elif Numero ==5:
	print "puede empesar a potencializar"
else: 
	print "Numero erroneo"
if Numero == 1:
	def suma():
		A = input("ingrese de A")
		B = input("ingrese de B")
		print A + B
	suma()
		