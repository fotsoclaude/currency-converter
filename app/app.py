from PySide2 import QtWidgets

# Définition de l'app
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        
    def setup_ui(self):
        #Orientation horizontale du layout
        self.layout = QtWidgets.QHBoxLayout(self)
        
        #Eléments du layout
        self.cbb_deviseFrom = QtWidgets.QComboBox() 
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
        
        #Ajout des éléments aux layout
        self.layout.addWidget(self.cbb_deviseFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
    
    
    
    

# création d'une application. Toujours passer une liste vide, si non on a une erreur*
app = QtWidgets.QApplication([])

# Création de la fenêtre || Instancier l'app
win = App()

# Affichage de la fenêtre
win.show()

# Exécution de l'application
app.exec_()