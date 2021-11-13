class Libro(object):
    def __init__(self):
        self.titulo = ""
        self.editor = ""
        self.numpaginas = 0
        self.anio = 0
        self.autor = ""

    def libro(self, titulo, editor, numpaginas, anio, autor):
        self.titulo = titulo
        self.editor = editor
        self.numpaginas = numpaginas
        self.anio = anio
        self.autor = autor

    def settitulo(self, titulo):
        self.titulo = titulo

    def seteditor(self, editor):
        self.editor = editor

    def setnumpaginas(self,numpaginas):
        self.numpaginas = numpaginas

    def setanio(self,anio):
        self.anio = anio

    def setautor(self, autor):
        self.autor = autor

    def gettitulo(self):
        return self.titulo

    def geteditor(self):
        return self.editor

    def getnumpaginas(self):
        return self.numpaginas

    def getanio(self):
        return self.anio

    def getautor(self):
        return self.autor

l = Libro()
l.settitulo('Harry Potter y la piedra filosofal')
l.setautor('J.K.Rowling')
l.setnumpaginas(220)
l.seteditor('Salamandra')
l.setanio(2001)

print(l.gettitulo())
print(l.getautor())
print(l.getnumpaginas())
print(l.geteditor())
print(l.getanio())