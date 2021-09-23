from __future__ import annotations
from typing import List



class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items() ] )
        return f"{self.__class__.__name__}({params})"

    def __repr__(self):
        return self.__str__()


class Address(StringReprMixin):
    def __init__(self, street: str, number: int) -> None:
        self.street = street
        self.number = number

class Person(StringReprMixin):
    def __init__(self, firstname:str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []
    
    def add_address(self, address: Address) -> None:
        self.addresses.append(address)


if __name__ == "__main__":
    bruno = Person("Bruno", "Fioreze")
    bruno_endereco = Address("Av. teste", "250A")
    bruno.add_address(bruno_endereco)
    print(bruno)
