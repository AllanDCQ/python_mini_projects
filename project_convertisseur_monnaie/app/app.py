from PySide2 import QtWidgets
import currency_converter


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.spn_montant = None
        self.setWindowTitle("Convertisseur de devises")

        self.layout = None
        self.cbb_devisesFrom = None
        self.cbb_devisesTo = None
        self.spn_montant = None
        self.spn_montantConverti = None
        self.btn_inverser = None

        self.setup_ui()
        self.set_default_values()
        self.setup_connections()
        self.setup_css()
        self.resize(600, 70)

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)

        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser les devises")

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)

    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))

        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")

        self.spn_montant.setRange(0, 1000000000)
        self.spn_montant.setValue(100)

        self.spn_montantConverti.setRange(0, 1000000000)
        self.spn_montantConverti.setValue(100)

    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)

        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)

    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        try:
            resultat = self.c.convert(montant,devise_from,devise_to)
        except:
            print("La conversion n'a pas fonctionné")
        else:
            self.spn_montantConverti.setValue(resultat)

    def inverser_devise(self):
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        montant = self.spn_montantConverti.value()

        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)
        self.spn_montant.setValue(montant)

        self.compute()

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30,30,30);
        color: rgb(240,240,240);
        border: none;
        """)
        self.btn_inverser.setStyleSheet("""
        background-color: rgb(240,240,240);
        color: rgb(30,30,30);
        """)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
