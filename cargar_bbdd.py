import sqlite3
import os

f_preguntas = open ('preguntas.txt', 'r',  encoding='utf-8-sig')


# Se define la posicion inicial (línea dentro del fichero) de la primera pregunta, opcion y respuesta. 
pos_prgta   = 1
pos_opcin   = 2
pos_rpsta   = 3
contador_pregunta = 1
CATEGORIA = 'Farmacologia'
preguntas = []

cont_lin = 0

list_item = []

for lin in f_preguntas:      

    

    if  lin[0] == 'P':
        list_item.append(contador_pregunta)
        pregunta = lin[3:]
        list_item.append(pregunta)
        contador_pregunta = contador_pregunta + 1
        
    elif lin[0] == 'O':
        opciones= lin[3:]
        list_item.append(opciones)
    else:
        respuesta= lin[3:]
        list_item.append(opciones)
        list_item.append(CATEGORIA)

    cont_lin = cont_lin +1 

    if cont_lin % 3 == 0:
        preguntas.append(list_item)        
        list_item = []


connection = sqlite3.connect('preguntas.db')

#create cursor to manage bd
cursor = connection.cursor()

# Crea la tabla gta (relasess de los juegos)
cursor.execute("create table preguntas (num_preg integer, encabezado text, opciones text, respuesta text, categoria text)")

cursor.executemany('insert into preguntas values (?, ?, ?, ?, ?) ', preguntas)

connection.commit()

# for row in cursor.execute ("select * from preguntas"):
#     print (row)


# os.system('cls')
# print ('*' * 20)
# for pregunta in preguntas:
#     for elmemento in pregunta:
#         print (elmemento, end="|| ")
#     print ()


