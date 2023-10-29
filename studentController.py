"""
    Módulo para modelar (Criar e Buscar) um aluno
"""

from utils import *
from databaseController import *


def get_infos():
    """
        Funçãoo usada para pegar as informações do cliente para um novo cadastro de um aluno

        Retorno:
            - Retorna o objeto do aluno
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
    student = get_infos()

    if check_if_exist(student):
        print(f"O(A) aluno(a) {student['name']} já foi cadastrado(a)!")
        return

    student["id"] = id

    return student


def get_student_by_id(id: int) -> dict:
    students = load_students()

    for student in students:
        if student['id'] == id:
            return student

    return 0


def filter_students_by_BMI() -> list:
    students = load_students()

    newStudents = []

    for student in students:
        if (calculate_BMI(student['weight'], student['height']) > 30):
            newStudents.append(student)

    return newStudents


def show_students(students):
    msg = ""

    for student in students:
        msg += f"Aluno: {student['name']} ID {student['id']} - Sexo: {describe_gender(student['gender'])} - Peso: {student['weight']}kg - Altura: {convert_to_meters(student['height'])} metros - Mensalidade: {student['subscription']}\n"

    print(msg)
