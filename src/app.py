import random
import matplotlib.pyplot as plt
from Benchmarking import BenchMarking
from SortMethods import MetodosOrdenamiento

class App:
    def __init__(self):
        self.metodos = MetodosOrdenamiento()
        self.benchmark = BenchMarking()
        self.tamaños = [5000, 10000, 30000, 50000, 100000]
        self.arreglo_base = self.generar_arreglo_base(max(self.tamaños))

    def generar_arreglo_base(self, tamaño_maximo):
        return [random.randint(1, 10000) for _ in range(tamaño_maximo)]

    def ejecutar_pruebas(self):
        tiempos_burbujamejorado = []
        tiempos_burbuja = []
        tiempos_seleccion = []
        tiempos_shell = []
        tiempos_insercion = []

        for tamaño in self.tamaños:
            arreglo_original = self.arreglo_base[:tamaño]
            
            # Probar Bubble Sort Mejorado
            arreglo_bubble = arreglo_original.copy()  
            tiempo_bubble = self.benchmark.medir_tiempo(self.metodos.burbujamejorado, arreglo_bubble)
            tiempos_burbujamejorado.append(tiempo_bubble)
            print(f"Tiempo Bubble Sort Mejorado para {tamaño} elementos: {tiempo_bubble:.6f} segundos")

            # Probar Bubble Sort Clásico
            arreglo_burbuja = arreglo_original.copy()  
            tiempo_burbuja = self.benchmark.medir_tiempo(self.metodos.burbuja, arreglo_burbuja)
            tiempos_burbuja.append(tiempo_burbuja)
            print(f"Tiempo Bubble Sort Clásico para {tamaño} elementos: {tiempo_burbuja:.6f} segundos")

            # Probar Selection Sort
            arreglo_selection = arreglo_original.copy()  
            tiempo_selection = self.benchmark.medir_tiempo(self.metodos.seleccion, arreglo_selection)
            tiempos_seleccion.append(tiempo_selection)
            print(f"Tiempo Selection Sort para {tamaño} elementos: {tiempo_selection:.6f} segundos")

            # Probar Shell Sort
            arreglo_shell = arreglo_original.copy()  
            tiempo_shell = self.benchmark.medir_tiempo(self.metodos.shell_sort, arreglo_shell)
            tiempos_shell.append(tiempo_shell)
            print(f"Tiempo Shell Sort para {tamaño} elementos: {tiempo_shell:.6f} segundos")

            # Probar Insertion Sort
            arreglo_insercion = arreglo_original.copy()  
            tiempo_insercion = self.benchmark.medir_tiempo(self.metodos.insercion, arreglo_insercion)
            tiempos_insercion.append(tiempo_insercion)
            print(f"Tiempo Insertion Sort para {tamaño} elementos: {tiempo_insercion:.6f} segundos")

       
        self.graficar_tiempos(tiempos_burbujamejorado, tiempos_burbuja, tiempos_seleccion, tiempos_shell, tiempos_insercion)

    def graficar_tiempos(self, burbujamejorado, burbuja, seleccion, shell, insercion):
        plt.figure(figsize=(10, 6))
        plt.plot(self.tamaños, burbujamejorado, marker='o', label='Bubble Sort Mejorado')
        plt.plot(self.tamaños, burbuja, marker='o', label='Bubble Sort Clásico')
        plt.plot(self.tamaños, seleccion, marker='o', label='Selection Sort')
        plt.plot(self.tamaños, shell, marker='o', label='Shell Sort')
        plt.plot(self.tamaños, insercion, marker='o', label='Insertion Sort')

        plt.title('Tiempos de Ejecucion de Algoritmos de Ordenamiento')
        plt.xlabel('Tamaño del arreglo')
        plt.ylabel('Tiempo (segundos)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('benchmark_results.png')
        print("Grafico guardado como 'benchmark_results.png'.")

# Ejecución de la aplicación
if __name__ == "__main__":
    app = App()
    app.ejecutar_pruebas()

