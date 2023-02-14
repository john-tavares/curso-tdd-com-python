from bytebank import Funcionario
from datetime import date

# Teste para verificar se a função idade() retorna a idade correta
def test_idade():
    funcionario = Funcionario('João', '01/01/1990', 5000)
    assert funcionario.idade() == date.today().year - 1990

# Teste para verificar se a função calcular_bonus() retorna o valor correto
def test_calcular_bonus():
    funcionario1 = Funcionario('João', '01/01/1990', 5000)
    assert funcionario1.calcular_bonus() == 500

    funcionario2 = Funcionario('Maria', '01/01/1990', 20000)
    assert funcionario2.calcular_bonus() == 0

# Teste para verificar se a função __str__() retorna a string correta
def test_to_string():
    funcionario = Funcionario('João', '01/01/1990', 5000)
    assert str(funcionario) == 'Funcionario(João, 01/01/1990, 5000)'

# Teste para verificar se o salário receberá decréscimo
def test_decrescimo_salario():
    salario1 = 5000
    funcionario1 = Funcionario('Ryan', '01/01/1990', salario1)
    assert funcionario1.salario == salario1

    salario2 = 100000
    funcionario2 = Funcionario('Jonathan', '01/01/1990', salario2)
    assert funcionario2.salario == salario2 * 0.9