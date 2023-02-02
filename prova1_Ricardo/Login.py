
import sys, cadastroAdm, MenuAdm, MenuUser
import psycopg2
from conexaoBanco import *
from PyQt5.QtWidgets import QLineEdit, QGridLayout, QPushButton, \
    QLabel, QMainWindow, QApplication, QWidget, QSizePolicy, QMessageBox, QTextBrowser


class telaLogin(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.widgetCentral = QWidget()
        self.setWindowTitle("Realize seu Login")
        self.setFixedSize(400,300)
        self.grid = QGridLayout(self.widgetCentral)

        self.labelLogin = QLabel("Usuário: ")
        self.labelLogin.setStyleSheet('font-size: 13px;')
        self.grid.addWidget(self.labelLogin, 1, 0, 1, 1)

        self.labelUser = QLineEdit()
        self.grid.addWidget(self.labelUser, 2, 0, 1, 1)
        self.labelUser.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.labelUser.setStyleSheet('font-size: 20px;')

        self.labelPassword = QLabel("Senha: ")
        self.labelPassword.setStyleSheet('font-size: 13px;')
        self.labelPassword.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.labelPassword, 3, 0, 1, 1)

        self.labelPass = QLineEdit()
        self.grid.addWidget(self.labelPass, 4, 0, 1, 1)
        self.labelPass.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.labelPass.setStyleSheet('font-size: 20px;')
        self.btn = QPushButton("CONFIRMAR")
        self.btn.setStyleSheet('font-size: 15px; background: blue; color: white;')
        self.btn.clicked.connect(self.validarDados)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 5, 0, 1, 1)

        self.setCentralWidget(self.widgetCentral)

    def mensagemErro(self, title, msg):
        msgErro = QMessageBox()
        msgErro.setWindowTitle(title)
        msgErro.setText(msg)
        msgErro.setStyleSheet('font-size: 15px; color: red;')
        msgErro.setStandardButtons(QMessageBox.Ok)
        msgErro.exec_()


    def validarDados(self, cont):
        if self.labelUser.text() == "" or self.labelPass.text() == "":
            return self.mensagemErro('Erro', 'Campoa inválidos\nPreencha-os novamente!')
        else:
            conecta = Conexao()
            usuario = self.labelUser.text()
            senha = self.labelPass.text()
            ativo = 'ATIVO'
            if usuario == 'admin':
                menuAdm = MenuAdm.telaMenuAdm(self)
                sql = f"select senha from usuario where login = '{usuario}'"
                resultado = conecta.executaDDL(sql)
                if resultado == []:
                    return self.mensagemErro('Erro', 'Usuario não encontrado!')
                elif senha == resultado [0][0]:
                    print("LOGIN ADMINISTRADOR REALIZADO COM SUCESSO!")
                    dado = f"insert into acao values ('001', '19/10/2022', '{usuario}', 'LOGIN ADM')"
                    conecta.executaDML(dado)
                    return menuAdm.show()
            else:
                menuUs = MenuUser.telaMenuAdm(self)
                sql = f"select senha from usuario where login = '{usuario}'"
                atv = f"select ativo from usuario where login = '{usuario}'"
                resultado = conecta.executaDDL(sql)
                resultadoAtv = conecta.executaDDL(atv)

                if resultado == []:
                    return self.mensagemErro('Erro', 'Usuario não encontrado!')
                if senha == resultado[0][0] and ativo ==  resultadoAtv[0][0]:
                    print("LOGIN REALIZADO COM SUCESSO!")
                    dado = f"insert into acao values ('002', '19/10/2022', '{usuario}', 'LOGIN')"
                    conecta.executaDML(dado)
                    return menuUs.show()
                else:
                    if cont == 3:
                        inativo = 'INATIVO'
                        up = f"update usuario set ativo where = '{inativo}'"
                        conecta.executaDML(up)
                    cont += 1
                    return self.mensagemErro('Erro', 'Senha inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = telaLogin()
    app.show()
    qt.exec_()
