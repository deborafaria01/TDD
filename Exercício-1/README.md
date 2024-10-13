# Exercício 1 - TDD PersonDAO Project

Este projeto foi desenvolvido utilizando a técnica de TDD (Test-Driven Development) para validar um objeto `Person` e seus e-mails associados, de acordo com as seguintes regras:

- O nome deve conter ao menos duas partes e ser composto por letras.
- A idade deve estar no intervalo de [1, 200].
- A pessoa deve ter pelo menos um objeto `Email` associado.
- O e-mail deve estar no formato "nome@dominio.com".

## Estrutura do Projeto

O projeto contém três arquivos principais:

- **person.py**: Implementa as classes `Person` e `Email`.
- **person_dao.py**: Implementa a classe `PersonDAO` e o método `isValidToInclude()`, responsável pelas validações.
- **test_person.py**: Contém os testes unitários utilizando o framework `unittest` para validar as regras aplicadas no método `isValidToInclude()`.

## Requisitos

- Python 3.8 ou superior
- Biblioteca `unittest` (inclusa na biblioteca padrão do Python)
  
## Instruções de Build

1. Certifique-se de que você tem o Python 3.8 ou superior instalado.

## Executando os Testes

1. Execute o seguinte comando dentro da pasta Exercício-1 para rodar os testes:

   ```bash
   python -m unittest test_person.py
