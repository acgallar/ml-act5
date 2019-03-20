import numpy as np

def hist_diff(var1, var2):
    h1, _ = np.histogram(var1, bins=100) # estimamos la frecuencia de obs. en 100 espacios definidos
    h2, _ = np.histogram(var2, bins=100) # estimamos la frecuencia de obs. en 100 espacios definidos
    get_minima = np.minimum(h1, h2) # extraemos el mínimo de observaciones comunes entre h1 y h2
    intersection = np.true_divide(np.sum(get_minima), np.sum(h2)) # Estimamos la intersección de elementos comunes
    return intersection