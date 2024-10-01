# 1 - Bibliotecas, framworks e referências externas
import pytest # framworks de teste de unidade

# funçoes que serao testadas (acrescentar a do exercicio)
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, calcular_area_do_quadrado

# 2 - Testes

def test_somar_doisnumeros():

    # padrão / standard AAA (se diz triple A / 3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura 
    # dados de entrada e saida
    num1 = 5
    num2 = 7 
    resultado_esperado = 12

    # Act / Executa 
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido 


def test_subtrair_doisnumeros():
    # Arrange
    num1 = 7
    num2 = 5 
    resultado_esperado = 2
    # Act / Executa 
    resultado_obtido = subtrair_dois_numeros(num1, num2)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido 

def test_multiplicar_doisnumeros():
    # Arrange
    num1 = 5
    num2 = 5   
    resultado_esperado = 25
    # Act / Executa 
    resultado_obtido = multiplicar_dois_numeros(num1, num2)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido 

def test_dividir_doisnumeros():
    # Arrange
    num1 = 15
    num2 = 5   
    resultado_esperado = 3
    # Act / Executa 
    resultado_obtido = dividir_dois_numeros(num1, num2)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido     

def test_calcular_area_do_quadrado():
    # Arrange
    lado = 6 
    resultado_esperado = 36
    # Act / Executa 
    resultado_obtido = calcular_area_do_quadrado(lado)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido      

def test_calcular_area_do_triangulo():
    # Arrange
    base = 6
    altura = 8
    resultado_esperado = 24    # (6 * 8) / 2
    # Act / Executa 
    resultado_obtido = calcular_area_do_triangulo(base, altura)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido    


