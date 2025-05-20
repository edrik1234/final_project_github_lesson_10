
import pandas as pd
import os
from Student import Student
from Person import Person
from Employee import Employee
from Options import Menu_Options
import library_functions as library


def save_new_entry(the_people_dictionary: dict, ages_sum: float, the_list_ids: list) -> float | None:
    user_id = library.is_in_dictionary(library.check_if_digit(library.try_input("please enter id: ")), the_people_dictionary)
    user_input = library.check_if_alpha(library.try_input("do you want to save a Person, Student, or Employee?: "))
    new_entry = None
    if user_input == "Person":
        new_entry = Person(user_id)
    elif user_input == "Student":
        new_entry = Student(user_id)
    elif user_input == "Employee":
        new_entry = Employee(user_id)
    else:
         print("invalid input please try again")
         return None
    the_people_dictionary[new_entry.get_id()] = new_entry
    the_list_ids.append(new_entry.get_id())
    ages_sum += the_people_dictionary[new_entry.get_id()].get_age()
    return ages_sum


def search_by_id(the_people_dictionary: dict) -> None:
    try:
        id_search = (library.check_if_digit(library.try_input("please enter the id that with him you want to search the current object: ")))
        print(f"the object in id {id_search}, is: {the_people_dictionary[id_search]}")
        return None
    except KeyError:
        print(f"invalid key pressed {id_search}. please try again key is not in dictionary")
    return None


def print_ages_avg(the_people_dictionary: dict, ages_sum: float) -> None:
    try:
        average = ages_sum/ len(the_people_dictionary)
        print("The ages average is: " + str(average) )  
        return None
    except ZeroDivisionError:
        print("we can't divide by zero please try again")
    return None


def print_all_names(the_people_dictionary: dict) -> None:
    for person in the_people_dictionary.values():
        print(person.get_name())
    return None


def print_all_ids(the_people_dictionary: dict) -> None:
    for person in the_people_dictionary.values():
        print(person.get_id())
    return None
 

def print_entry_by_index(the_people_dicitonary: dict, list_ids: list) -> None:
    index = library.check_if_digit(library.try_input("please enter the index  of value you want:"))
    try:   
        id = list_ids[index]
        print("the index is: " + str(index))
        print(f"the id of this index is: {id}. and the data is {the_people_dicitonary[id]}")
        return None
    except IndexError:
        print("index is out of range please try again ")
    except AttributeError:
        print(f"this attribute does not exist on this object: {index}")
    return None 


def print_entries(the_people_dicitionary: dict) -> None:
    for people in the_people_dicitionary.values():
        type_class = people.get_type_str() 
        print(f"the type of class is {type_class}")
        print(people)
    return None


def save_all_data(the_people_dictionary: dict) -> None:
    data_list = []
    for person in the_people_dictionary.values():
        value = person.get_as_dict()
        data_list.append(value)
    df = pd.DataFrame(data_list)
    file_name = input("What is your output file name? : ")
    output_path = os.path.join(file_name + ".csv")
    df.to_csv(output_path, index = False)
    print("Data saved successfully to " + output_path)
    return None

        
def print_menu() -> None:
    for item in Menu_Options:
        print(str(item.value) + ". " + item.name.replace("_", " ").title())
    return None
   

def run_main(people_dictionary_1, ages_sum_1, list_ids_1) -> None:
    while True:
        try:
            print_menu() 
            choose_option = Menu_Options(int(input("please choose an option:")))
            if choose_option == Menu_Options.Save_New_Entry:
                ages_sum_1 = save_new_entry(people_dictionary_1, ages_sum_1,list_ids_1)
            elif choose_option == Menu_Options.Search_By_Id:
                search_by_id(people_dictionary_1)
            elif choose_option == Menu_Options.Print_Ages_Avg:
                print_ages_avg(people_dictionary_1, ages_sum_1)
            elif choose_option == Menu_Options.Print_All_Names:
                print_all_names(people_dictionary_1)
            elif choose_option == Menu_Options.Print_All_Ids:
                print_all_ids(people_dictionary_1)
            elif choose_option == Menu_Options.Print_Entry_By_Index:
                print_entry_by_index(people_dictionary_1, list_ids_1 )
            elif choose_option == Menu_Options.Print_All_Entries_Using_Polymyarizm:
                print_entries(people_dictionary_1)
            elif choose_option == Menu_Options.Save_All_Data:
                save_all_data(people_dictionary_1)
            elif choose_option == Menu_Options.Exit:
                new_option = input("Are you sure?(y/n)?:")
                if new_option == 'y':
                    break
                else:
                    continue
        except KeyboardInterrupt:
            print("\nyou pressed ctrl+c please try again")
        except ValueError:
            print("incorrect value please try again")
        input("Press Enter to continue...")


list_ids = []
people_dictionary = {}
ages_sum = 0
run_main(people_dictionary, ages_sum, list_ids)
                                                                                                                                                                                                                                                                                                                                                                                                                                                          