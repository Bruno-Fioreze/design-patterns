from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items() ] )
        return f"{self.__class__.__name__}({params})"

    def __repr__(self):
        return self.__str__()

class User(StringReprMixin):

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []

    
class IUserBuilder(ABC):

    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_first_name(self, firstname): pass
    
    @abstractmethod
    def add_last_name(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass
    
    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(ABC):

    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self): 
        data = self._result
        self.reset()
        return data

    def add_first_name(self, firstname): 
        self._result.first_name = firstname
    
    def add_last_name(self, lastname): 
        self._result.lastname = lastname
        
    def add_age(self, age): 
        self._result.age = age

    def add_phone(self, phone): 
        self._result.phone_numbers.append(phone)

    def add_address(self, address): 
        self._result.addresses.append(address)


class UserDirector:
    def __init__(self, builder):
        self._builder: UserBuilder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_first_name(firstname)
        self._builder.add_last_name(lastname)
        self._builder.add_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address):
        self._builder.add_first_name(firstname)
        self._builder.add_last_name(lastname)
        self._builder.add_address(address)
        return self._builder.result

if __name__ == "__main__":
    user_builder = UserBuilder()
    user_diretor = UserDirector(user_builder)

    user_age = user_diretor.with_age("teste", "bruno", 25)
    print(user_age)

    user_address = user_diretor.with_address("teste", "bruno", "Av. teste")
    print(user_address)