
import sys, cadastroAdm, json
from conexaoBanco import *
from PyQt5.QtWidgets import QGridLayout, QPushButton, \
    QMainWindow, QApplication, QWidget, QSizePolicy, QMessageBox

class telaMenuAdm(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.widgetCentral = QWidget()
        self.setWindowTitle("MENU ADMINISTRATIVO")
        self.setFixedSize(300,300)
        self.grid = QGridLayout(self.widgetCentral)

        self.btn = QPushButton("CADASTRAR USUÁRIO")
        self.btn.setStyleSheet('font-size: 15px; background: darkblue; color: white;')
        self.btn.clicked.connect(self.cadastrarUsuario)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 1, 0, 1, 1)

        self.btn = QPushButton("CONSULTAR TRANSAÇÕES")
        self.btn.setStyleSheet('font-size: 15px; background: blue; color: white;')
        #self.btn.clicked.connect(self.exibirRelatorio)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 2, 0, 1, 1)

        self.btn = QPushButton("EXPORTAR ARQUIVO DE LOG")
        self.btn.setStyleSheet('font-size: 15px; background: darkblue; color: white;')
        self.btn.clicked.connect(self.gerarArquivo)
        self.btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 3, 0, 1, 1)


        self.setCentralWidget(self.widgetCentral)

    def mensagemSucesso(self, title, msg):
        msgScs = QMessageBox()
        msgScs.setWindowTitle(title)
        msgScs.setText(msg)
        msgScs.setStyleSheet('font-size: 15px; color: green;')
        msgScs.setStandardButtons(QMessageBox.Ok)
        msgScs.exec_()

    def cadastrarUsuario(self):
        cadastrar = cadastroAdm.telaCadAdm(self)
        cadastrar.show()

    def gerarArquivo(self):
        conecta = Conexao()
        sql = f"select * from acao"
        resultado = conecta.executaDDL(sql)
        codigo = resultado[0][0]
        data = resultado[0][1]
        user = resultado[0][2]
        ac = resultado[0][3]
        with open("arquivoLog.json", "r") as file:
            relatorio = file.read()
            relatorio = json.loads(relatorio)
        total = len(relatorio)
        arq = {
            f"Acao{total + 1}": {
                "CODIGO": codigo,
                "DATA": data,
                "USUARIO": user,
                "ACAO": ac
            },
        }
        relatorio.update(arq)
        relatorio_json = json.dumps(relatorio, indent=True)
        with open("arquivoLog.json", "w+") as file:
            file.write(relatorio_json)
        return self.mensagemSucesso('Sucesso', 'Arquivo gerado com sucesso!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = telaMenuAdm()
    app.show()
    qt.exec_()