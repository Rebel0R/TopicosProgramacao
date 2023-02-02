import sys
from conexaoBanco import *
from PyQt5.QtWidgets import QLineEdit, QGridLayout, QPushButton, \
    QLabel, QMainWindow, QApplication, QWidget, QSizePolicy, QMessageBox

class telaCadAdm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widgetCentral = QWidget()
        self.setWindowTitle("Cadastro de Usuário")
        self.setFixedSize(400, 300)
        self.grid = QGridLayout(self.widgetCentral)

        self.labelNome = QLabel('Login:')
        self.labelNome.setStyleSheet('font-size: 12px;')
        self.grid.addWidget(self.labelNome, 1, 0, 1, 1)
        self.labelLoginCad = QLineEdit()
        self.grid.addWidget(self.labelLoginCad, 2, 0, 1, 1)
        self.labelLoginCad.setStyleSheet('font-size: 20px;')

        self.labelSenha = QLabel('Senha:')
        self.labelSenha.setStyleSheet('font-size: 12px;')
        self.grid.addWidget(self.labelSenha, 3, 0, 1, 1)
        self.labelSenhaCad = QLineEdit()
        self.grid.addWidget(self.labelSenhaCad, 4, 0, 1, 1)
        self.labelSenhaCad.setStyleSheet('font-size: 20px;')


        self.labelDataR = QLabel('Data de Criação:')
        self.labelDataR.setStyleSheet('font-size: 12px;')
        self.grid.addWidget(self.labelDataR, 5, 0, 1, 1)
        self.labelDataRCad = QLineEdit()
        self.grid.addWidget(self.labelDataRCad, 6, 0, 1, 1)
        self.labelDataRCad.setStyleSheet('font-size: 20px;')

        self.btn = QPushButton('CADASTRAR')
        self.btn.setStyleSheet('font-size: 15px; background: darkblue; color: white;')
        self.btn.clicked.connect(self.cadastrarUsuarioBanco)
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

    def cadastrarUsuarioBanco(self):
        if self.labelLoginCad.text() == "" or self.labelSenhaCad.text() == "" or self.labelDataRCad == "":
            return self.mensagemErro('ERRO', 'Campo de Usuário ou Senha inválidos\nPreencha os campos!')

        else:
            login = self.labelLoginCad.text()
            senha = self.labelSenhaCad.text()
            ativo = 'ATIVO'
            dataC = self.labelDataRCad.text()
            conecta = Conexao()
            sql = f"insert into usuario values ('{login}', '{senha}', '{ativo}', '{dataC}')"
            conecta.executaDML(sql)
            return self.mensagemSucesso('CADASTRADO', 'Novo usuário cadastrado com sucesso!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = telaCadAdm()
    app.show()
    qt.exec_()