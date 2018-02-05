class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo da conta {}: {}".format(self.numero, self.saldo))

    def saca(self, valor):
        self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor