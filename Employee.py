
from Person import Person
import library_functions as library


class Employee(Person):
    def __init__(self, people_id) -> None:
        super().__init__(people_id)
        self.field_work = library.check_if_alpha(library.try_input("please enter employee's field_work: "))
        self.salary = library.check_if_digit(library.try_input("please enter employee's salary: "))


    def get_salary(self) -> int:
        return self.salary
    

    def get_field_work(self) -> str:
        return self.field_work
    

    def set_salary(self, new_salary) -> None:
        self._salary = library.check_if_digit(new_salary)


    def set_field_work(self, new_field_work) -> None:
        self._field_work = library.check_if_alpha(new_field_work)


    def print_myself(self) -> None:
        print( self.return_str_print_people() + "," + " the field of work is  " + self.get_field_work() + " and the salary is " + str(self.get_salary())) 


    def __str__(self) -> str: 
        return f"the information about the employee is: {self.return_str_print_people()}. the employe's salary is: {self.salary}. and finally the employe's field of work is: {self.field_work}"
    
    
    def get_as_dict(self) -> dict:
        all_dict = super().get_as_dict()
        all_dict["field_work"] = self.field_work
        all_dict["salary"] = self.salary
        return all_dict