from abc import ABC, abstractclassmethod

class Abstract(ABC):

    def template_method(self):
        self.hook()
        self.method_one()
        self.base_class_method()
        self.method_two()
    
    def hook(self): pass

    def base_class_method(self):
        print('OLÁ, EU SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM.')

    @abstractclassmethod
    def method_one(self) -> None: pass

    @abstractclassmethod
    def method_two(self) -> None: pass



class ConcreteClass(Abstract):

    def hook(self):
        print("Olha, eu vou utilizar o hook.")

    def method_one(self) -> None: 
        print("Método 1 concluído.")

    def method_two(self) -> None: 
        print("Método 2 concluído.")    


class ConcreteClassTwo(Abstract):
    def method_one(self) -> None: 
        print("Método 1 concluído ( ConcreteClassTwo ).")

    def method_two(self) -> None: 
        print("Método 2 concluído ( ConcreteClassTwo ) .")   


if __name__ == "__main__":

    c1 = ConcreteClass()
    c1.template_method()
    print()
    c1 = ConcreteClassTwo()
    c1.template_method()