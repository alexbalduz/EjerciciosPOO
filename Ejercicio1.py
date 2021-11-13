class Libro(object):
    def __init__(self):
        self.titulo = ""
        self.editor = ""
        self.numpaginas = 0
        self.año = 0
        self.autor = ""

    def libro(self, titulo, editor, numpaginas, año, autor):
        self.titulo = titulo
        self.editor = editor
        self.numpaginas = numpaginas
        self.año = año
        self.autor = autor

    def settitulo(self, titulo):
        self.titulo = titulo

    def seteditor(self, editor):
        self.editor = editor

    def setnumpaginas(self,numpaginas):
        self.numpaginas = numpaginas

    def setaño(self,año):
        self.anio = año

    def setautor(self, autor):
        self.autor = autor

    def gettitulo(self):
        return self.titulo

    def geteditor(self):
        return self.editor

    def getnumpaginas(self):
        return self.numpaginas

    def getaño(self):
        return self.año

    def getautor(self):
        return self.autor

l = Libro()
l.settitulo('Harry Potter y la piedra filosofal')
l.setautor('J.K.Rowling')
l.setnumpaginas(220)
l.seteditor('Salamandra')
l.setaño(2001)

print(l.gettitulo)
print(l.getautor)
print(l.getnumpaginas)
print(l.geteditor)
print(l.getaño)