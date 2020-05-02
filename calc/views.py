
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de tu app llamada calc.")
    
def calcular(request, operation, op1, op2):

	if operation == "sumar":
		return HttpResponse("El resultado es: " + str(op1+op2))
	
		
	elif operation == "restar":
		return HttpResponse("El resultado es: " + str(op1-op2))
	
	
	elif operation == "multiplicar":
		return HttpResponse("El resultado es: " + str(op1*op2))
	
	
	elif operation == "dividir":
		try:
			result = (op1/op2)
			return HttpResponse("El resultado es: " + str(result))
			
		except ZeroDivisionError:
			return HttpResponse ("No se puede dividir entre 0")
			
		
	else:
		return HttpResponse("Operacion invalida introduzca {sumar, restar, multiplicar, dividir}")
	

