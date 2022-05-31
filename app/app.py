from PySide2 import QtWidgets

# Définition de l'app
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devises")

# création d'une application. Toujours passer une liste vide, si non on a une erreur*
app = QtWidgets.QApplication([])

# Création de la fenêtre
win = App()

# Affichage de la fenêtre
win.show()

# Exécution de l'application
app.exec_()