class LinkedList:
	def __init__(self):
		#inicializo la cabecera nula
		self.head = None

    def insertar(self, nodo_nuevo):
    	#compruebo si la cabecera es nula o no
		if self.head:
			#cogemos el último nodo
			last_node = self.head
			while last_node != None:
				last_node = last_node.next

			#asignamos el nuevo nodo al siguiente punto del ultimo nodo
			last_node.next = nodo_nuevo

		else:
			#cabecera esta vacía
			#asignamos nodo a la cabecera
			self.head = nodo_nuevo

    def mostrar(self):
    	#variable para iterar
		temp_node = self.head

		#iteramos hasta que llegamos al final de la lista
		while temp_node != None:
			#printamos el nodo data
			print(temp_node.data, end='->')

			#nos movemos al siguiente nodo
			temp_node = temp_node.next

		print('Null')