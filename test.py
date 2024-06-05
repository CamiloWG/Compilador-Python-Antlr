import math
from collections import Counter

def calcular_entropia_palabras(file_path):
    # Leer el contenido del archivo
    with open(file_path, 'r', encoding='utf-8') as file:
        texto = file.read()
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Contar la frecuencia de cada palabra en el texto
    conteo = Counter(palabras)
    print('Conteo:', conteo)
    total_palabras = len(palabras)
    
    # Calcular la probabilidad de cada palabra
    probabilidades = [freq / total_palabras for freq in conteo.values()]
    
    # Calcular la entropía
    entropia = -sum(p * math.log2(p) for p in probabilidades)
    
    return entropia

# Ejemplo de uso
file_path = 'quijote.txt'

entropia = calcular_entropia_palabras(file_path)
print(f'La entropía del texto es: {entropia}')
