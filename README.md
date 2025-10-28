🧑‍💻 Python OOP Project – Person, Student & Employee Management

This project is a Python Object-Oriented Programming (OOP) application that allows users to manage and interact with Person, Student, and Employee objects through a menu-driven interface. It demonstrates key OOP concepts such as inheritance, polymorphism, and encapsulation, and includes input validation, error handling, and data export functionalities.

🔹 Features

Create New Entries: Add Person, Student, or Employee objects with validated input.

Search & Access Data: Search by ID, access objects by index, or list all names and IDs.

Polymorphism: Display all objects showing their type and attributes.

Calculate Statistics: Compute the average age of all stored entries.

Data Persistence: Save all data to a CSV file using pandas for future use.

Robust Input Handling: Includes validation for digits, alphabetic input, and handles invalid keys or indices gracefully.

Menu Interface: Interactive console menu dynamically generated from Menu_Options enum.



🧪 Automated Testing (Newly Added)

A comprehensive pytest test suite was added to ensure the reliability and correctness of all project components.
The test file (module_testing_script.py) includes:

Helper Function Tests (library_functions.py):
Validation of numeric and alphabetic input functions, ensuring proper looping on invalid inputs using unittest.mock.patch to simulate user input.

Class Tests (Person, Student, Employee):
Verification of object initialization, setters/getters, type correctness, and string representation behavior.

Integration Tests (final_project_of_python.py):
Testing key program functions such as:

save_new_entry (data creation and dictionary updates)

search_by_id (invalid ID handling)

print_ages_avg (zero division safety)

print_all_names / print_all_ids (output correctness)

print_entry_by_index (index validity)

print_entries (polymorphic output)

save_all_data (CSV creation and save verification)

These tests use mocked input, captured stdout (capsys), and temporary file handling to fully automate validation without requiring user interaction.

✅ Result: The test suite verifies both unit-level and integration-level correctness, ensuring stable and maintainable code quality.


🛠️ Technologies & Concepts

Python 3

Object-Oriented Programming (OOP) concepts:

Inheritance (Student and Employee inherit from Person)

Polymorphism (shared interface for all objects)

Encapsulation (private attributes with getter methods)

Modules: pandas, os, pytest, unittest.mock

Input validation and error handling

CSV export and data management

Automated testing and mocking

📁 Project Structure

Person.py – Base class representing a generic person.

Student.py – Subclass representing a student.

Employee.py – Subclass representing an employee.

Options.py – Enum defining menu options for the interface.

library_functions.py – Helper functions for input validation and dictionary operations.

final project of python.py – Main file that runs the program and integrates all modules.

module_testing_script  - Automated test suite (pytest).

Key Learning Outcomes✅

Solid understanding of OOP principles in Python.

Experience in menu-driven application design.

Handling data validation, error management, and CSV exports.

Demonstrated ability to combine multiple modules into a cohesive project.

Writing automated unit and integration tests using pytest and mock.

Ensuring maintainability through test coverage and clean architecture.
