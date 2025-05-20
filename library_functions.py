def check_if_digit(value) -> int:
    while not value.isdigit(): 
        print("The value: " + str(value) + " isn't a number please try again")
        value = input("Enter a valid value: ")  
    return int(value)   


def try_input(prompt: str) -> str | None :
    try:
        input_value = input(prompt)
        return input_value
    except KeyboardInterrupt:
        print("you have pressed ctrl + c we are now exiting")
        return None
    

def check_if_alpha(user_input: str) -> str:
    while not user_input.isalpha():
        print("this input  isn't a string try to type again please")
        user_input = input("please enter again and please enter a correct string: ")
    return str(user_input)


def is_in_dictionary(key, dictionary) -> int:
    while key in dictionary:
        print("the value is in dictionary please type id again: ")
        key = check_if_digit(try_input("please enter a normal value: "))
    return key
