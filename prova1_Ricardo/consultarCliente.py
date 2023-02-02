import sys
from conexaoBanco import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QMainWindow, QApplication, QWidget, QTextBrowser


class telaConsultaCliente(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.widgetCentral = QWidget()
        self.setWindowTitle("Clientes Existentes no banco")
        self.setFixedSize(400,500)
        self.grid = QGridLayout(self.widgetCentral)

        self.labelTitulo = QLabel("CLIENTES")
        self.labelTitulo.setStyleSheet('font-size: 13px; color: darkblue;')
        self.grid.addWidget(self.labelTitulo, 0, 0, 1, 1)

        self.consulta = QTextBrowser()
        self.grid.addWidget(self.consulta, 1, 0, 1, 1)

        conecta = Conexao()
        sql = "select * from cliente"

        resultado = conecta.executaDDL(sql)
        for col in resultado:
            self.consulta.append(f'CPF: {col[0]}  Nome: {col[1]}  Email: {col[2]}')
            self.consulta.append('----------------------------------------------------\n')

        self.setCentralWidget(self.widgetCentral)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = telaConsultaCliente()
    app.show()
    qt.exec_()