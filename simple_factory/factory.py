from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de popular está buscando o cliente...")



class VeiculoFactory:

    @staticmethod
    def get_carro( tipo: str ) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        if tipo == "popular":
            return CarroPopular()
        
        assert 0, "Véiculo não existe."


if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ["luxo", "popular"]

    for i in range(1, 10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()