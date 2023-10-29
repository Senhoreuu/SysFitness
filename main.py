from header import *
from databaseController import *
from studentController import *

id = get_last_id()
students = load_students()


def choice_option():
    """
        Função que exibe o menu e chama as funções de acordo com a opção escolhida
    """
    while True:
        print_header()
        display_menu()

        option = input("Escolha uma opção: ")

        # Checando a opção escolhida
        if (option == '1'):
            clear_screen()
            student = create_student(id)

            if not student:
                continue

            students.append(student)

        elif (option == '2'):
            clear_screen()
            show_students(students)

        elif (option == '3'):
            clear_screen()
            show_student(students)

        elif (option == '4'):
            clear_screen()
            filter_students_by_BMI(students)

        elif (option == '5'):
            clear_screen()
            save_students(students)
            print("Dados salvos com sucesso! Tchau!")
            break

        else:
            clear_screen()
            print("A opção escolhida é inválida. Tente novamente")


def main():
    choice_option()


main()
