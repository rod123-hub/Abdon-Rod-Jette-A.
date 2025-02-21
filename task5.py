class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by ₱{amount:.2f}. New salary: ₱{self.salary:.2f}")
        else:
            print("Raise amount must be positive.")
    
    def display_employee(self):
        print("Employee Details:")
        print(f"  Name    : {self.name}")
        print(f"  Position: {self.position}")
        print(f"  Salary  : ₱{self.salary:.2f}")

employee = Employee("Rod Jette", "Software Engineer", 60000)

employee.display_employee()

raise_amount = float(input("Enter raise amount: "))
employee.give_raise(raise_amount)

employee.display_employee()
