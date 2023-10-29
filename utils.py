import os


def read_integer(msg="", positive=False):
    """
    Realiza a leitura de de um valor inteiro, tratando possíveis erros

    Parâmetros:
        - msg: Mensagem a ser exibida antes da leitura. Por padrão "" (vazia)
        - pos: flag que indica a leitura apenas de um número positivo ou não. Por padrão False.

    Retorno:
    - Valor inteiro lido do teclado
    """
    while True:
        try:
            value = int(input(msg))
            if not positive:
                return value
            else:
                if value >= 0:
                    return value
                else:
                    print("Entrada de dados em formato inválido! Digite novamente: ")
        except:
            print("Entrada de dados em formato inválido! Digite novamente: ")


def read_float(msg="", positive=False):
    """
    Realiza a leitura de de um valor real, tratando possíveis erros

    Parâmetros:
        - msg: Mensagem a ser exibida antes da leitura. Por padrão "" (vazia)
        - pos: flag que indica a leitura apenas de um número positivo ou não. Por padrão False.

    Retorno:
        - Valor real lido do teclado
    """
    while True:
        try:
            value = float(input(msg))
            if not positive:
                return value
            else:
                if value >= 0:
                    return value
                else:
                    print("Entrada de dados em formato inválido! Digite novamente: ")
        except:
            print("Entrada de dados em formato inválido! Digite novamente: ")


def describe_gender(gender: str) -> str:
    if gender == 'f':
        return 'Feminino'
    elif gender == 'm':
        return 'Masculino'
    elif gender == 'o':
        return 'Não binárie'


def convert_to_meters(cm: int) -> float:
    return cm / 100


def calculate_BMI(weight, height):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura.

    Parâmetros:
        - weight: Peso em quilogramas.
        - height: Altura em metros.

    Retorno:
        - Retorna o valor do IMC
    """
    bmi = weight / (height ** 2)
    return bmi


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
