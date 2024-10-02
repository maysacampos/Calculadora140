# 1 - Bibliotecas, framworks e referências externas
import pytest # framworks de teste de unidade

# funçoes que serao testadas (acrescentar a do exercicio)
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, calcular_area_do_quadrado, calcular_area_do_retangulo, calcular_area_do_triangulo

from utils.utils import ler_csv    # função de leitura de arquivo csv

# 2 - Testes

def test_somar_dois_numeros():

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


def test_subtrair_dois_numeros():
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

def test_dividir_por_zero():
    # Arrange
    num1 = 15
    num2 = 0  
    resultado_esperado = 'Erro: Não é possível dividir por zero'
    # Act / Executa 
    resultado_obtido = dividir_dois_numeros(num1, num2)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido     

# Exercicio 1
def test_calcular_area_do_quadrado():
    # Arrange
    lado = 6 
    resultado_esperado = 36
    # Act / Executa 
    resultado_obtido = calcular_area_do_quadrado(lado)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido      

# Exercicio 1
def test_calcular_area_do_retangulo():
    # Arrange
    base = 6
    altura = 5
    resultado_esperado = 30    # (6 * 8) 
    # Act / Executa 
    resultado_obtido = calcular_area_do_retangulo(base, altura)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido    

# Exercicio 1
def test_calcular_area_do_triangulo():
    # Arrange
    base = 6
    altura = 8
    resultado_esperado = 24    # (6 * 8) / 2
    # Act / Executa 
    resultado_obtido = calcular_area_do_triangulo(base, altura)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido  


# Teste Baseados em Dados = data Driven Tests (DDT)
    # Dados em uma lista
    # Dados em um arquivo, vários formatos: csv (tesxto separado por virgula), json, xml, dat

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [
                          (5, 7, 12),   
                          (0, 8, 8),
                          (10, -15, -5),
                          (6, 0.75, 6.75)
                         ]
                        )

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):

    # padrão / standard AAA (se diz triple A / 3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura 
    # dados de entrada e saida fornecidos pela massa de teste em formato de lista

    # Act / Executa 
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido 

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                           ler_csv('./fixtures/massa_somar.csv')
                         )

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):

    # padrão / standard AAA (se diz triple A / 3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura 
    # dados de entrada e saida fornecidos pela massa de teste em formato de lista

    # Act / Executa 
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido 

# Teste Baseados em Dados = data Driven Tests (DDT)


# Exercicio 2

@pytest.mark.parametrize('lado, resultado_esperado',
                         [
                          (6, 36),
                          (5, 25),
                          (15, 225),
                          (12, 144)
                         ]
                        )


def test_calcular_area_do_quadrado_lista(lado, resultado_esperado):
       
    # Act / Executa 
    resultado_obtido = calcular_area_do_quadrado(lado)
    # Assert / Valida
    assert resultado_esperado == resultado_obtido  

# Exercicio 3

@pytest.mark.parametrize('lado, resultado_esperado',
                         ler_csv('./fixtures/massa_area_quadrado.csv')
                         )

def test_calcular_area_do_quadrado_csv(lado, resultado_esperado):
       
    # Act / Executa 
    resultado_obtido = calcular_area_do_quadrado(int(lado))
    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido  

