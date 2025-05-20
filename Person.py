
import library_functions as library


class Person:
    _id = None
    _name = None
    _age = None
    def __init__(self, people_id) -> None:
        self._name = library.check_if_alpha(library.try_input("please enter  name: "))
        self._age = library.check_if_digit(library.try_input("please enter  age: "))
        self._id = people_id


    def get_age(self) -> int:
        return self._age


    def get_name(self) -> str:
        return self._name


    def get_id(self) -> int:
        return self._id


    def set_age(self, new_age) -> None:
        self._age = library.check_if_digit(new_age)


    def set_id(self, new_id) -> None:
        self._id = library.check_if_digit(new_id)


    def set_name(self, new_name) -> None:
        self._name = library.check_if_alpha(new_name)
   

    def return_str_print_people(self) -> str:
        return "the id of " + self.get_name() + " is : " + str(self.get_id()) + " and the age is " + str(self.get_age())

   
    def print_myself(self) -> None:
        print(self.return_str_print_people()) 
    

    def get_type_str(self) -> str:
        return self.__class__.__name__


    def __str__(self) -> str: 
        return f' the person`s name: {self._name}. the person`s age: {self._age}. the person`s id: {self._id}.'
    
    
    def get_as_dict(self) -> dict:
        all_dict = {}
        all_dict["id"] = self._id
        all_dict["age"] = self._age
        all_dict["name"] = self._name
        return all_dict


