# hello
class Employee:
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def print_employees(self):
        for emp in self.employees:
            print(emp)


def main():
    database = EmployeeDatabase()

    while True:
        print("\n1. Add Employee")
        print("2. Sort by Age")
        print("3. Sort by Name")
        print("4. Sort by Salary")
        print("5. Print Employees")
        print("6. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, age, salary)
            database.add_employee(employee)
        elif choice == 2:
            database.sort_by_age()
        elif choice == 3:
            database.sort_by_name()
        elif choice == 4:
            database.sort_by_salary()
        elif choice == 5:
            database.print_employees()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()