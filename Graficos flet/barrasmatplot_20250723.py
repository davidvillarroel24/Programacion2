import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt

def main(page: ft.Page):

    # Crear figura con Matplotlib

    fig, ax = plt.subplots()

    fruits = ['lunes', 'martes', 'miercoles', 'jueves','viernes']
    counts = [60, 40, 80, 75,20]
    bar_labels = ['red', 'blue', '_red', 'orange','yellow']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:green']

    #ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Consumo KWh')
    ax.set_title('Comsumo electrico por dia')
    ax.legend(title='Colores')

    #plt.show()



    # Mostrar gráfico en Flet
    chart = MatplotlibChart(fig, expand=True)

    page.add(chart)

ft.app(target=main)