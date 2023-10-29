from header import *
from databaseController import *
from studentController import *

id = get_last_id()
students = load_students()


def choice_option():
    while True:
        display_menu()

        option = input("Escolha uma opção: ")

        # Checando a opção escolhida
        if (option == '1'):
            student = create_student(id)
            
            if not student:
                continue

            students.append(student)

        elif (option == '2'):
            show_students(students)

        elif (option == '3'):
            _id = read_integer(msg="Insira o ID: ", positive=True)
            student = get_student_by_id(_id)

            if student:
                print(f"Aluno: {student['name']} ID {student['id']} - Sexo: {describe_gender(student['gender'])} - Peso: {student['weight']}kg - Altura: {convert_to_meters(student['height'])} metros - Mensalidade: {student['subscription']}")
            else:
                print(f"O(A) aluno(a) com o id {_id} não existe!")

        elif (option == '4'):
            filter_students_by_BMI()

        elif (option == '5'):
            save_students(students)
            break

        else:
            print("A opção escolhida é inválida. Tente novamente")
            
        clear_screen()


def main():
    print_header()
    choice_option()


main()
