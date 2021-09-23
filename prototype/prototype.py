from __future__ import annotations
from typing import List


class Address:
    def __init__(self, street: str, number: int) -> None:
        self.street = street
        self.number = number

class Person:
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
