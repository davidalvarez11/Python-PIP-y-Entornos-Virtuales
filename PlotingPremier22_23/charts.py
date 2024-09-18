import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bestmfbyclub():
    mfpass= pd.read_csv('Data/MfComparissionPass.csv')
    mfpasstop50 = mfpass.head(50)

    # Generar la gráfica de barras
    ax = mfpasstop50.groupby('club').size().plot(kind='bar', color='skyblue', edgecolor='black')

    # Personalizar la gráfica
    ax.set_title('Distribución del TOP50 MF', fontsize=15, fontweight='bold')
    ax.set_xlabel('Club', fontsize=12)
    ax.set_ylabel('Cantidad', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Mostrar la gráfica
    plt.savefig('Charts/BestMFByClub.png')
    plt.close()