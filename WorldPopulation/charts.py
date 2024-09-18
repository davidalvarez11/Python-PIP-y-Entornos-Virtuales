# primero importamos la libreria de matplotlib
# y la llamamos de otra forma para no tener
# que usar ese nombre tan largo

import matplotlib.pyplot as plt
import numpy as ny

# creamos la función para generar la
# grafica de barra
def generate_bar_chart(name,labels, values):
    # le damos cuales van a ser los valores 
    # y los labels de esa grafica
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # le digo al programa que grafique
    plt.savefig(f'./charts/{name}.png')

# Generamos la función para la creación de
# una grafica circular, en forma de torta
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
    values = [8436152, 13055050, 732555, 4383123, 11124910]
    print(values)
    generate_pie_chart(labels, values)
    generate_bar_chart(labels, values)