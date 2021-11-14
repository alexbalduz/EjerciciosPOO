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