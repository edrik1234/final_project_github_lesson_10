from Person import Person
import library_functions as library


class Student(Person):
    def __init__(self, people_id) -> None:
        super().__init__(people_id)
        self.field_study = library.check_if_alpha(library.try_input("please enter student's field of study: "))
        self.year_study = library.check_if_digit(library.try_input("please enter student's year of study: "))
        self.score_average = library.check_if_digit(library.try_input("please enter student's score average: "))


    def get_field_of_study(self) -> str:
        return self.field_study


    def get_year_study(self) -> int:
        return self.year_study


    def get_score_average(self) -> int:
        return self.score_average


    def set_field_study(self, new_field_study) -> None:
        self._field_study = library.check_if_alpha(new_field_study)


    def set_year_study(self, new_year_study) -> None:
        self._year_study = library.check_if_digit(new_year_study)


    def set_score_average(self, new_score_average) -> None:
        self._score_average = library.check_if_digit(new_score_average)


    def print_myself(self) -> str:
        print(self.return_str_print_people() + "," + " the field of study is " + self.get_field_of_study() + " and year of study is " + str(self.get_year_study()) + " and the average score is " + str(self.get_score_average()))
    
   
    def get_type_str(self) -> str:
        return self.__class__.__name__


    def __str__(self) -> str:
        return f"the information about student is: {self.return_str_print_people()}. Student's field of study: {self.field_study}. Student's year of study {self.year_study}. And finally Student's Average sccore {self.score_average}"
    
    
    def get_as_dict(self) -> dict:
        all_dict = super().get_as_dict()
        all_dict["field_study"] = self.field_study
        all_dict["year_study"] = self.year_study
        all_dict["score_average"] = self.score_average
        return all_dict
            