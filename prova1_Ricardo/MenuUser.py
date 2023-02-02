import sys, cadastroCliente, consultarCliente
from PyQt5.QtWidgets import QLineEdit, QGridLayout, QPushButton, \
    QLabel, QMainWindow, QApplication, QWidget, QSizePolicy, QMessageBox

class telaMenuAdm(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.widgetCentral = QWidget()
        self.setWindowTitle("MENU USUÁRIO")
        self.setFixedSize(300,300)
        self.grid = QGridLayout(self.widgetCentral)

        self.btn = QPushButton("CADASTRAR CLIENTE")
        self.btn.setStyleSheet('font-size: 15px; background: darkblue; color: white;')
        self.btn.clicked.connect(self.cadastrarCliente)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 1, 0, 1, 1)

        self.btn = QPushButton("CONSULTAR CLIENTE")
        self.btn.setStyleSheet('font-size: 15px; background: blue; color: white;')
        self.btn.clicked.connect(self.consultarClientes)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 2, 0, 1, 1)

        self.setCentralWidget(self.widgetCentral)

    def cadastrarCliente(self):
        cadastrar = cadastroCliente.telaCadCl(self)
        cadastrar.show()

    def consultarClientes(self):
        consultar = consultarCliente.telaConsultaCliente(self)
        consultar.show()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = telaMenuAdm()
    app.show()
    qt.exec_()