
import re

class PersonDAO:
    @staticmethod
    def isValidToInclude(person):
        errors = []
        
        # Validação do nome
        if len(person.name.split()) < 2 or not all(part.isalpha() for part in person.name.split()):
            errors.append("O nome deve ter pelo menos duas partes e ser composto apenas por letras.")
        
        # Validação da idade
        if not (1 <= person.age <= 200):
            errors.append("A idade deve estar entre 1 e 200.")
        
        # Validação de e-mails
        if not person.emails:
            errors.append("A pessoa deve ter pelo menos um email associado.")
        else:
            email_regex = r'^[^@]+@[^@]+\.[^@]+$'
            for email in person.emails:
                if not re.match(email_regex, email.name):
                    errors.append(f"O email {email.name} não está no formato correto.")
        
        return errors
