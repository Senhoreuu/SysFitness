import json

def save_students(students):
    """
        Salva os dados no banco de dados (students.json)
    """
    with open('students.json', 'w') as file:
        json.dump(students, file)
    
    
def load_students() -> dict:
    """
        Carrega os dados do banco de dados (students.json)
    """
    with open('students.json', 'r') as file:
        data = json.load(file)
    return data

def check_if_exist(student: dict):
    """
        Checa se o aluno já está cadastrado no banco de dados (students.json)
        
        Parâmetro:
            - student: Objeto do aluno
            
        Retorno: 
            - Retorna se existe ou não (0 = False, 1 = True)
        
    """
    data = load_students()
    for i in data:
        if i['name'] == student['name']:
            return 1
    return 0

def get_last_id() -> int:
    """
        Retorna o último id cadastrado no banco de dados (students.json)
    """
    data = load_students()
    
    return len(data) if len(data) > 0 else 1 