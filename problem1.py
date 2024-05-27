"""
Write a program to get user input of employees and their id, age and salary and form a dictionary.

Example : { "<emp1_name>" :{"ID": 001, "Age":25, "Salary":25000}, "<emp2_name>" :{"ID": 002, "Age":27, "Salary":25000}, ... }
"""


def EmployeeData():
    masterEmployee = {}
    count_emp = int(input("Enter the Number of Employees for which you want to enter the data "))

    for i in range(1, count_emp + 1):
        print(f"Enter the details of employee {i} \t")
        empName = input("Enter the Employee's Name")
        empID = input("ID : ")
        empAge = int(input("Age (in years) : "))
        empSalary = input("Enter the Salary : ")

        masterEmployee[empName] = {"ID": empID, "Age": empAge, "Salary": empSalary}

    print(masterEmployee)


"""
implement a method in python to convert the temperature in Celsius into degrees Fahrenheit using decorators(getter|setter).
      Note : the temperature of any object cannot reach below -273.15 degrees Celsius
      1. Convert human temperature in Celsius to Fahrenheit. (Formula - (temp*1.8)+32 )
      2. Provide invalid temperature and handle the exception.
"""


class Temp:
    def __init__(self):
        self._celsius = None

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, val):
        if val < -273.15:
            raise ValueError("Temperature cannot be set less than 273.15 degree celsius")
        self._celsius = val

    @property
    def tempFahrenheit(self):
        if self._celsius is None:
            return None
        val1 = (self._celsius*1.8) + 32
        return val1


try :
    objTemp = Temp()

    objTemp.celsius = float(input("Enter the temperature in celsius"))
    print("Temperature in celsius : ", objTemp.celsius)
    print("Temperature in Fahrenheit : ", objTemp.tempFahrenheit)

except Exception as e:
    print(e)





