import eel
import os  
from tkinter import Tk
from tkinter.filedialog import askdirectory
#from db.db_manager import insert_paciente, get_pacientes

eel.init('web')

root = Tk()
root.withdraw()

@eel.expose
def select_directory():
    directory = askdirectory()
    return directory


@eel.expose
def save_paciente(nome, dataNascimento, sexo, dataExame):
    #insert_paciente(nome, dataNascimento, sexo, dataExame) #salva no banco de dados
    return "Paciente salvo!"


@eel.expose
def store_data(nome, dataNascimento, sexo, dataExame, directory):

    dir_name = f"{nome}_{dataNascimento}_{sexo}_{dataExame}"
    dir_name = dir_name.replace(":", "_").replace("-", "_")  

    #caminho onde a pasta será criada
    path = os.path.join(directory, 'data', dir_name)

    #criacao da pasta se ela não existir
    if not os.path.exists(path):
        os.makedirs(path)

    #caminho do arquivo dentro da pasta criada
    file_path = os.path.join(path, 'data.txt')

    #dados no arquivo dentro da pasta específica
    with open(file_path, 'a') as file:
        file.write(f"Nome: {nome}, Idade: {dataNascimento}, Sexo: {sexo}, Data do exame: {dataExame}\n")

    eel.show('confirmacao.html') 

eel.start('Info-Paciente.html') # eel.start('web/Info-Paciente.html', size=(700, 600))
