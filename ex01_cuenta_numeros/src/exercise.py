def main():
    # IPO (Entrada–Proceso–Salida):
    # Entrada:
    # N
    # Proceso (2–4 pasos):
    # 1. Leer n
    # 2. i = 1
    # 3. Mientras i < n
    #         Mostrar i
    #         i = i +1
    # Salida:
    # 1..n
    #
    # Invariante del ciclo:
    # Al iniciar el ciclo i, ya mostré los valores hasta i-1
    #
    # PROMPTS IA (si usaste) + cambios + verificación manual:
    #
    # PROMPT: Explicame la estructura típica del uso de un contador hasta un valor n usando while
    # CAMBIOS: 
    # VERIFICACION: Probé con valores n=0, n=1, n>1
    # Escribe tu solución abajo de esta línea
    n = int(input())
    i = 1
    while i <= n:
        print(i)
        i = i + 1


if __name__ == '__main__':
    main()

# REFLEXION CORTA
# 1. La parte del problema que me resultó más mecánica fué la lectura de los datos de ENTRADA
# 2. Al usar la IA, la limitación que tuve fue diseñar el prompt de forma tal que su respuesta me ayude a encontrar la solución a mi problema.
# 3. Validando que ciertos procesos que requieren cuenta, se enumeren de forma ascendente uno por uno