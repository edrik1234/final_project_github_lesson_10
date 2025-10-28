import pytest
from unittest.mock import patch
import final_project_of_python as final
from Person import Person
from Student import Student
from Employee import Employee
import library_functions as library


# --------------------------
# בדיקות פונקציות עזר (library_functions)
# --------------------------

def test_check_if_digit_valid():
    assert library.check_if_digit("123") == 123

@patch("builtins.input", side_effect=["abc", "456"])
def test_check_if_digit_invalid_then_valid(mock_input, capsys):
    result = library.check_if_digit("abc")  # ייכנס ללולאה עד שמוקלט "456"
    captured = capsys.readouterr().out
    assert "isn't a number" in captured
    assert result == 456


def test_check_if_alpha_valid():
    assert library.check_if_alpha("hello") == "hello"

@patch("builtins.input", side_effect=["123", "world"])
def test_check_if_alpha_invalid_then_valid(mock_input, capsys):
    result = library.check_if_alpha("123")
    captured = capsys.readouterr().out
    assert "isn't a string" in captured
    assert result == "world"


# --------------------------
# בדיקות למחלקות Person / Student / Employee
# --------------------------

def test_person_basic():
    p = Person(1)
    p.set_name("Alice")
    p.set_age("25")
    assert p.get_id() == 1
    assert p.get_name() == "Alice"
    assert p.get_age() == 25
    assert isinstance(p.get_as_dict(), dict)
    assert "Alice" in str(p)


def test_student_basic():
    with patch("builtins.input", side_effect=["Bob", "20", "CS", "2", "85"]):
        s = Student(2)
        assert s.get_name() == "Bob"
        assert s.get_field_of_study() == "CS"
        assert s.get_year_study() == 2
        assert s.get_score_average() == 85


def test_employee_basic():
    with patch("builtins.input", side_effect=["Charlie", "30", "IT", "10000"]):
        e = Employee(3)
        assert e.get_name() == "Charlie"
        assert e.get_field_work() == "IT"
        assert e.get_salary() == 10000


# --------------------------
# בדיקות לפונקציות ב-final_project_of_python
# --------------------------

@patch("builtins.input", side_effect=["1", "Person", "David", "40"])
def test_save_new_entry_person(mock_input):
    people_dict = {}
    ages_sum = 0
    ids = []
    result = final.save_new_entry(people_dict, ages_sum, ids)
    assert result == 40
    assert 1 in people_dict
    assert isinstance(people_dict[1], Person)


@patch("builtins.input", side_effect=["99"])
def test_search_by_id_invalid(mock_input, capsys):
    people_dict = {1: Person(1)}
    final.search_by_id(people_dict)
    captured = capsys.readouterr().out
    assert "invalid key pressed" in captured


def test_print_ages_avg_zero_division(capsys):
    final.print_ages_avg({}, 0)
    captured = capsys.readouterr().out
    assert "can't divide by zero" in captured


def test_print_all_names_and_ids(capsys):
    p = Person(1)
    p.set_name("Eve")
    p.set_age("22")
    d = {1: p}
    final.print_all_names(d)
    final.print_all_ids(d)
    captured = capsys.readouterr().out
    assert "Eve" in captured
    assert "1" in captured


@patch("builtins.input", side_effect=["0"])
def test_print_entry_by_index_valid(mock_input, capsys):
    p = Person(1)
    p.set_name("Mike")
    p.set_age("33")
    final.print_entry_by_index({1: p}, [1])
    captured = capsys.readouterr().out
    assert "the id of this index is: 1" in captured


@patch("builtins.input", side_effect=["5"])
def test_print_entry_by_index_out_of_range(mock_input, capsys):
    final.print_entry_by_index({}, [])
    captured = capsys.readouterr().out
    assert "index is out of range" in captured


def test_print_entries(capsys):
    p = Person(1)
    p.set_name("Zara")
    p.set_age("28")
    final.print_entries({1: p})
    captured = capsys.readouterr().out
    assert "the type of class is Person" in captured
    assert "Zara" in captured


patch("builtins.input")
def test_save_all_data(tmp_path, mock_input, capsys):
    mock_input.side_effect = [str(tmp_path / "test_output")]
    p = Person(1)
    p.set_name("Neo")
    p.set_age("40")
    d = {1: p}
    final.save_all_data(d)
    captured = capsys.readouterr().out
    assert "Data saved successfully" in captured
    assert (tmp_path / "test_output.csv").exists()  # לוודא שהקובץ באמת נוצר
