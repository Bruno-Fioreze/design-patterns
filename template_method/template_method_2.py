from abc import ABC, abstractclassmethod

class Pizza(ABC):

    def prepare(self) -> None:
        """ Template Method. """
        self.hook_before_add_ingredients() # Hook
        self.add_ingrentients() # Abstract
        self.cook() # Abstract
        self.cut()  # Concrete
        self.serve() # Concrete

    def hook_before_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f"{self.__class__.__name__} - Cortando a pizza.")
    
    def serve(self) -> None:
        print(f"{self.__class__.__name__} - Servindo a pizza.")

    @abstractclassmethod
    def add_ingrentients(self): pass

    @abstractclassmethod
    def cook(self): pass

class StylishPizza(Pizza):

    def add_ingrentients(self) -> None: 
        print(f"StylishPizza - Adicionando ingredientes: presunto, queijo e goiabada.")

    def cook(self) -> None: 
        print(f"StylishPizza - Cozinhando por 45 minutos no forno.")



class Veg(Pizza):

    def hook_before_add_ingredients(self) -> None:
        print("Veg - Lavando ingredientes.")

    def add_ingrentients(self) -> None: 
        print(f"Veg - Adicionando ingredientes: ingredientes veganos.")

    def cook(self) -> None: 
        print(f"Veg - Cozinhando por 45 minutos no forno normal.")


if __name__ == "__main__":
    a_moda = StylishPizza()
    a_moda.prepare()

    print()
    veg = Veg()
    veg.prepare() 