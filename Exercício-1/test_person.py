
import unittest
from person import Person, Email
from person_dao import PersonDAO

class TestPersonDAO(unittest.TestCase):

    def test_valid_person(self):
        emails = [Email(1, "teste@teste.com")]
        person = Person(1, "John Doe", 30, emails)
        errors = PersonDAO.isValidToInclude(person)
        self.assertEqual(len(errors), 0)

    def test_invalid_name(self):
        emails = [Email(1, "teste@teste.com")]
        person = Person(1, "John", 30, emails)
        errors = PersonDAO.isValidToInclude(person)
        self.assertIn("O nome deve ter pelo menos duas partes e ser composto apenas por letras.", errors)

    def test_invalid_age(self):
        emails = [Email(1, "teste@teste.com")]
        person = Person(1, "John Doe", 300, emails)
        errors = PersonDAO.isValidToInclude(person)
        self.assertIn("A idade deve estar entre 1 e 200.", errors)

    def test_no_email(self):
        person = Person(1, "John Doe", 30, [])
        errors = PersonDAO.isValidToInclude(person)
        self.assertIn("A pessoa deve ter pelo menos um email associado.", errors)

    def test_invalid_email_format(self):
        emails = [Email(1, "testeteste.com")]
        person = Person(1, "John Doe", 30, emails)
        errors = PersonDAO.isValidToInclude(person)
        self.assertIn("O email testeteste.com não está no formato correto.", errors)

if __name__ == '__main__':
    unittest.main()
