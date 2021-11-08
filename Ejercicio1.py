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