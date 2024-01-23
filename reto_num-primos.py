# Función que verifica si un número es primo
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función que guarda los números primos en un archivo dentro de un rango especificado
def guardar_primos_en_archivo(nombre_archivo, inicio, fin):
    with open(nombre_archivo, "w") as f:
        contador_primos = 0
        # Itera sobre el rango [max(2, inicio), fin]
        for num in range(max(2, inicio), fin + 1):
            if primo(num):
                # Escribe el número primo en el archivo y lo imprime
                f.write(str(num) + "\n")
                print(num)
                contador_primos += 1
        # Devuelve la cantidad de números primos encontrados
        return contador_primos

# Función que verifica si los resultados en el archivo coinciden con los números primos esperados en el rango
def verificar_resultados(nombre_archivo, inicio, fin):
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
        # Genera los resultados esperados para el rango dado
        resultados_esperados = "\n".join(str(num) for num in range(max(2, inicio), fin + 1) if primo(num)) + "\n"
        # Compara los resultados esperados con los resultados reales en el archivo
        if resultados_esperados == contenido:
            print("El script produjo los resultados esperados.")
        else:
            print("El script no produjo los resultados esperados.")

# Función que cuenta y muestra la cantidad de números primos en un archivo
def contar_primos_en_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
        numeros_primos = [int(line) for line in contenido.split("\n") if line.isdigit()]
        cantidad_primos = len(numeros_primos)
        # Muestra la cantidad de números primos en el archivo
        print(f"En el archivo hay {cantidad_primos} números primos.")
        return cantidad_primos

# Punto de entrada principal
if __name__ == "__main__":
    # Nombre del archivo de resultados
    nombre_archivo_resultados = "results.txt"
    # Rango de números para buscar primos
    inicio_rango = 1
    fin_rango = 250

    # Llama a la función para guardar primos en el archivo y obtiene la cantidad de primos
    cantidad_primos = guardar_primos_en_archivo(nombre_archivo_resultados, inicio_rango, fin_rango)
    # Llama a la función para verificar si los resultados son correctos
    verificar_resultados(nombre_archivo_resultados, inicio_rango, fin_rango)
    # Llama a la función para contar y mostrar la cantidad de primos en el archivo
    
    contar_primos_en_archivo(nombre_archivo_resultados)

