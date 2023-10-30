from header import *
from databaseController import *
from studentController import *


def choice_option():
    id = get_last_id()
    students = load_students()

    """
        Função que exibe o menu e chama as funções de acordo com a opção escolhida
    """
    while True:
        print_header()
        display_menu()

        option = input("Escolha uma opção: ")

        clear_screen()

        # Checando a opção escolhida
        if (option == '1'):
            student = create_student(id)

            if not student:
                continue
            
            id += 1

            students.append(student)

        elif (option == '2'):
            show_students(students)

        elif (option == '3'):
            show_student(students)

        elif (option == '4'):
            filtreds = filter_students_by_BMI(students)
            show_students(filtreds)

        elif (option == '5'):
            save_students(students)
            print("Dados salvos com sucesso! Tchau!")
            break

        else:
            print("A opção escolhida é inválida. Tente novamente")


def main():
    choice_option()


main()
