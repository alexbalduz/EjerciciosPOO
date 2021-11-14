class LinkedList:
	def __init__(self):
		#inicializo la cabecera nula
		self.head = None

    def insertar(self, nodo_nuevo):
    		#compruebo si la cabecera es nula o no
		if self.head:
			#cogemos el último nodo
			last_node = self.head
			while last_node.next != None:
				last_node = last_node.next

			#asignamos el ultimo nodo al anterior del nuevo nodo
			nodo_nuevo.prev = last_node

			#asignamos el nuevo nodo al siguiente del ultimo nodo
			last_node.next = nodo_nuevo

    def mostrar(self):

		#printamos la data en orden normal
		print("Orden normal: ", end='')

		temp_node = self.head
		while temp_node != None:
			print(temp_node.data, end=' ')
			temp_node = temp_node.next
		print()

		#printamos la data en orden inverso
		print("Orden inverso: ", end='')

		#cogemos el ultimo nodo
		last_node = self.head
		while last_node.next != None:
			last_node = last_node.next

		temp_node = last_node
		while temp_node != None:
			print(temp_node.data, end=' ')
			temp_node = temp_node.prev
		print()