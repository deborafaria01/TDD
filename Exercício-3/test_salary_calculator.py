
import unittest
from employee import Employee
from salary_calculator import SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):

    def test_developer_high_salary(self):
        employee = Employee("John Doe", "john@example.com", 4000, "DESENVOLVEDOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 4000 * 0.8)

    def test_developer_low_salary(self):
        employee = Employee("Jane Doe", "jane@example.com", 2500, "DESENVOLVEDOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 2500 * 0.9)

    def test_dba_high_salary(self):
        employee = Employee("Jake Doe", "jake@example.com", 2500, "DBA")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 2500 * 0.75)

    def test_dba_low_salary(self):
        employee = Employee("Jill Doe", "jill@example.com", 1500, "DBA")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 1500 * 0.85)

    def test_tester_high_salary(self):
        employee = Employee("Jack Doe", "jack@example.com", 2500, "TESTADOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 2500 * 0.75)

    def test_tester_low_salary(self):
        employee = Employee("Janet Doe", "janet@example.com", 1500, "TESTADOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 1500 * 0.85)

    def test_manager_high_salary(self):
        employee = Employee("Joe Doe", "joe@example.com", 6000, "GERENTE")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 6000 * 0.7)

    def test_manager_low_salary(self):
        employee = Employee("Jodie Doe", "jodie@example.com", 4000, "GERENTE")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 4000 * 0.8)

if __name__ == '__main__':
    unittest.main()
