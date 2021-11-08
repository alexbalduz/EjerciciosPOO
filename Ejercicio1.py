class Libro(object):
    def __init__(self):
        self.titulo = ""
        self.editor = ""
        self.numpaginas = ""
        self.año = ""
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
        self.numpaginas=numpaginas

    def setanio(self,anio):
        self.anio=anio

    def setanio(self,anio):
        self.anio=anio
