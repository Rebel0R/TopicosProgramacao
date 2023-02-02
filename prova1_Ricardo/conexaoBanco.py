import psycopg2


class Conexao():
    def __init__(self, host = "localhost", db = "postgres",
                 user = "postgres", password="1234"):
        self.host = host
        self.db = db
        self.usuario = user
        self.senha = password

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(host=self.host,
                                            database=self.db,
                                            user=self.usuario,
                                            password=self.senha)
            self.cursor = self.conexao.cursor()
            print("Conectado ao Banco")

        except Exception as e:
            print("Erro de conexao")
            print(e)

    def desconectar(self):
        self.conexao.close()
        print("Desconectado do PostgreSQL")

    def executaDDL(self, sql):
        self.conectar()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.desconectar()
        return resultado

    def executaDML(self, sql):
        self.conectar()
        self.cursor.execute(sql)
        self.conexao.commit()
        self.desconectar()