import sys
from conexaoBanco import *
from PyQt5.QtWidgets import QLineEdit, QGridLayout, QPushButton, \
    QLabel, QMainWindow, QApplication, QWidget, QSizePolicy, QMessageBox

class telaCadCl(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widgetCentral = QWidget()
        self.setWindowTitle("Cadastro de Cliente")
        self.setFixedSize(400, 300)
        self.grid = QGridLayout(self.widgetCentral)

        self.labelCPF = QLabel('CPF:')
        self.labelCPF.setStyleSheet('font-size: 12px;')
        self.grid.addWidget(self.labelCPF, 1, 0, 1, 1)
        self.labelCPFCad = QLineEdit()
        self.grid.addWidget(self.labelCPFCad, 2, 0, 1, 1)
        self.labelCPFCad.setStyleSheet('font-size: 20px;')

        self.labelNome = QLabel('Nome:')
        self.labelNome.setStyleSheet('font-size: 12px;')
        self.grid.addWidget(self.labelNome, 3, 0, 1, 1)
        self.labelNomeCad = QLineEdit()
        self.grid.addWidget(self.labelNomeCad, 4, 0, 1, 1)
        self.labelNomeCad.setStyleSheet('font-size: 20px;')


        self.labelEmail = QLabel('Email:')
        self.labelEmail.setStyleSheet('font-size: 12px;')
        self.grid.addWidget(self.labelEmail, 5, 0, 1, 1)
        self.labelEmailCad = QLineEdit()
        self.grid.addWidget(self.labelEmailCad, 6, 0, 1, 1)
        self.labelEmailCad.setStyleSheet('font-size: 20px;')

        self.btn = QPushButton('CADASTRAR')
        self.btn.setStyleSheet('font-size: 15px; background: darkblue; color: white;')
        self.btn.clicked.connect(self.cadastrarClienteBanco)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.grid.addWidget(self.btn, 7, 0, 1, 1)

        self.setCentralWidget(self.widgetCentral)

    def mensagemErro(self, title, msg):
        msgErro = QMessageBox()
        msgErro.setWindowTitle(title)
        msgErro.setText(msg)
        msgErro.setStyleSheet('font-size: 15px; color: red;')
        msgErro.setStandardButtons(QMessageBox.Ok)
        msgErro.exec_()

    def mensagemSucesso(self, title, msg):
        msgScs = QMessageBox()
        msgScs.setWindowTitle(title)
        msgScs.setText(msg)
        msgScs.setStyleSheet('font-size: 15px; color: green;')
        msgScs.setStandardButtons(QMessageBox.Ok)
        msgScs.exec_()

    def cadastrarClienteBanco(self):
        if self.labelCPFCad.text() == "" or self.labelNomeCad.text() == "" or self.labelEmailCad == "":
            return self.mensagemErro('ERRO', 'Campos inválidos ou vázios!\nPreencha-os novamente!')

        else:
            cpf = self.labelCPFCad.text()
            nome = self.labelNomeCad.text()
            email = self.labelEmailCad.text()
            conecta = Conexao()
            sql = f"insert into cliente values ('{cpf}', '{nome}', '{email}')"
            conecta.executaDML(sql)
            return self.mensagemSucesso('CADASTRADO', 'Novo Cliente cadastrado com sucesso!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = telaCadCl()
    app.show()
    qt.exec_()