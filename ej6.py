#Metodo normal
def normalizar(lista, modo):
    nueva_lista = []
    
    if len(lista) == 0:
        return nueva_lista

    if modo == "minmax":
        minimo = lista[0]
        maximo = lista[0]
        for x in lista:
            if x < minimo:
                minimo = x
            if x > maximo:
                maximo = x
        
        diferencia = maximo - minimo
        if diferencia == 0:
            print("Error: División por cero (max igual a min)")
            return lista[:]
            
        for x in lista:
            valor = (x - minimo) / diferencia
            nueva_lista.append(valor)

    elif modo == "zscore":
        suma = 0
        for x in lista:
            suma += x
        promedio = suma / len(lista)
        
        suma_cuadrados = 0
        for x in lista:
            suma_cuadrados += (x - promedio) ** 2
        desviacion = (suma_cuadrados / len(lista)) ** 0.5
        
        if desviacion == 0:
            print("Error: División por cero (desviación estándar es 0)")
            return lista[:]
            
        for x in lista:
            valor = (x - promedio) / desviacion
            nueva_lista.append(valor)

    elif modo == "unit":
        suma_cuadrados = 0
        for x in lista:
            suma_cuadrados += x ** 2
        norma = suma_cuadrados ** 0.5
        
        if norma == 0:
            print("Error: División por cero (norma es 0)")
            return lista[:]
            
        for x in lista:
            valor = x / norma
            nueva_lista.append(valor)
            
    else:
        print("Modo no válido")
        return lista[:]

    return nueva_lista

valores = [10, 20, 30]

print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print(f"Lista dada: {valores}")


#Con numpy
import numpy as np

def normalizar(lista, modo):
    arr = np.array(lista, dtype=float)
    
    if modo == "minmax":
        minimo = np.min(arr)
        maximo = np.max(arr)
        if maximo - minimo == 0:
            return list(arr)
        res = (arr - minimo) / (maximo - minimo)
        
    elif modo == "zscore":
        desviacion = np.std(arr)
        if desviacion == 0:
            return list(arr)
        promedio = np.mean(arr)
        res = (arr - promedio) / desviacion
        
    elif modo == "unit":
        norma = np.linalg.norm(arr)
        if norma == 0:
            return list(arr)
        res = arr / norma
        
    else:
        print("Modo no válido")
        return list(arr)
        
    return res.tolist()



print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print(f"Lista dada: {valores}")
