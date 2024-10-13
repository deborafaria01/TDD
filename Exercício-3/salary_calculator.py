
class SalaryCalculator:
    
    @staticmethod
    def calculate_net_salary(employee):
        if employee.role == "DESENVOLVEDOR":
            if employee.base_salary >= 3000:
                return employee.base_salary * 0.8
            return employee.base_salary * 0.9
        elif employee.role == "DBA" or employee.role == "TESTADOR":
            if employee.base_salary >= 2000:
                return employee.base_salary * 0.75
            return employee.base_salary * 0.85
        elif employee.role == "GERENTE":
            if employee.base_salary >= 5000:
                return employee.base_salary * 0.7
            return employee.base_salary * 0.8
        else:
            raise ValueError("Cargo desconhecido")
