# importo el modulo nativo de python para
# importar csv
import csv

# definimos la función que nos va a leer el
# archivo con la ubicacion (path) que le
# demos
def read_csv(ubicacion):
    # abrimos el archivo con permiso solo de 
    # lectura ('r') en este caso
    with open(ubicacion,'r') as csvfile:
        # con la funcion nativa reader del modulo
        # csv, leemos el csv que en este caso 
        # biene delimitado con comas, verificar que
        # si este delimitado con coma.
        reader = csv.reader(csvfile, delimiter=',')
        # sabemos la primera fila es la del 
        # encabezado, por lo que la sacaremos
        # manualmente con next
        first_row = next(reader)
        # como queremos una lista con diccionarios
        # creamos la lista data.
        data=[]
        for row in reader:
            # utilizamos zip para unir los encabezados
            # con las filas que se están iterando y
            # obtenemos los pares, lista de tuplas
            iterable = zip(first_row, row)
            # con las tuplas generamos un diccionario con
            # el formato de dictionary comprehension
            country_dict = {key: value for key, value in iterable}
            # cada diccionario lo incluimos en la lista data
            # que habiamos creado anteriormente
            data.append(country_dict)
        return data
    

if __name__ == '__main__':
    data = read_csv('world_population.csv')
    print(data)