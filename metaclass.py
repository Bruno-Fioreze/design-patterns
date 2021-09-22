class Meta(type):
    def __call__(cls, *args, **kwargs):
        print("CALL é chamado primeiro")
        return super().__call__(*args, **kwargs)

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("Cria o objeto")
        return super().__new__(cls)
     
    def __init__(self, nome):
        self.nome = nome
        print("Inicializa o objeto")

    def __call__(self, x, y):
        print("Call Chamado", self.nome, x + y)

p1 = Pessoa("Luiz")
p1(1, 2)
print(p1.nome)