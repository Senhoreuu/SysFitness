"""
    Módulo para modelar (Criar e Buscar) um aluno
"""

from utils import *
from databaseController import *


def get_infos() -> dict:
    """
        Funçãoo usada para pegar as informações do cliente para um novo cadastro de um aluno

        Retorno:
            - Retorna o objeto do aluno criado
    """
    student = {}

    while True:
        student["name"] = input('Nome do(a) Aluno(a): ')

        if len(student["name"]) <= 2:
            clear_screen()
            print(
                f"{student['name']} não é um nome aceito! Digite um nome válido.")
            continue

        student["gender"] = input(
            'Digite o sexo do(a) aluno(a) (M - Masculino, F - Feminino, O - Não binárie): ').lower()

        if student["gender"] not in ["f", "m", "o"]:
            clear_screen()
            print(
                f"{student['gender']} não é um sexo aceito! Digite um sexo válido (M, F, O)")
            continue

        student["weight"] = read_float(
            msg='Digite o peso do(a) aluno(a) em (Kg): ', positive=True)
        student["height"] = read_integer(
            msg='Digite a altura do(a) aluno(a) em (cm): ', positive=True)
        student["subscription"] = read_float(
            msg='Digite a mensalidade: ', positive=True)

        break

    return student


def create_student(id: int) -> dict:
    """
        Função usada para criar um novo aluno
        
        Parâmetro:
            - id: id do aluno
            
        Retorno:
            - Retorna o objeto do aluno criado
    """
    student = get_infos()

    if check_if_exist(student):
        print(f"O(A) aluno(a) {student['name']} já foi cadastrado(a)!")
        return

    student["id"] = id

    return student


def get_student_by_id(id: int, students: dict) -> dict:
    """
        Função usada para buscar um aluno por id
        
        Parâmetros:
            - id: id do aluno
            - students: lista de alunos
            
        Retorno:
            - Retorna o objeto do aluno encontrado ou 0 se não existir
    """
    for student in students:
        if student['id'] == id:
            return student

    return 0


def filter_students_by_BMI(students: dict) -> list:
    """
        Função usada para filtrar os alunos com base no IMC maior que 30
        
        Parâmetros:
            - students: lista de alunos
            
        Retorno:
            - Retorna uma lista com os alunos com o IMC maior que 30
    """
    newStudents = []

    for student in students:
        if (calculate_BMI(student['weight'], student['height']) > 30):
            newStudents.append(student)

    return newStudents


def show_students(students):
    """
        Função usada para exibir todos os alunos cadastrados
        
        Parâmetros:
            - students: lista de alunos
    """
    msg = ""

    for student in students:
        msg += f"Aluno: {student['name']} ID {student['id']} - Sexo: {describe_gender(student['gender'])} - Peso: {student['weight']}kg - Altura: {convert_to_meters(student['height'])} metros - Mensalidade: {student['subscription']} reais\n"

    print(msg)


def show_student(students: dict):
    """
        Função usada para exibir um aluno específico
        
        Parâmetros:
            - students: lista de alunos
    """
    id = read_integer(msg="Insira o ID: ", positive=True)
    student = get_student_by_id(id, students)
    
    if student:
        print(f"Aluno: {student['name']} ID {student['id']} - Sexo: {describe_gender(student['gender'])} - Peso: {student['weight']}kg - Altura: {convert_to_meters(student['height'])} metros - Mensalidade: {student['subscription']} reais")
    else:
        print(f"O(A) aluno(a) com o id {id} não existe!")
