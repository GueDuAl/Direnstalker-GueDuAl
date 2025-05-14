import tkinter as tk
from tkinter import messagebox

def calcular_diferencia():
    try:
        hora_inicio = entrada_hora_inicio.get()
        hora_fin = entrada_hora_fin.get()

        # Parsea las horas y minutos
        hora_inicio, minutos_inicio = map(int, hora_inicio.split(":"))
        hora_fin, minutos_fin = map(int, hora_fin.split(":"))

        # Calcula la diferencia de horas y minutos
        horas_pasadas = hora_fin - hora_inicio
        minutos_pasados = minutos_fin - minutos_inicio

        # Ajusta los minutos si son negativos
        if minutos_pasados < 0:
            minutos_pasados += 60
            horas_pasadas -= 1

        # Muestra el resultado en la misma ventana
        resultado_var.set(f"Entre las {hora_inicio}:{minutos_inicio:02d} y las {hora_fin}:{minutos_fin:02d} han pasado:\n"
                          f"{horas_pasadas} horas y {minutos_pasados} minutos.")

    except ValueError:
        resultado_var.set("Ingresa las horas en el formato correcto (HH:MM).")

def sumar_valores():
    try:
        valor1 = entrada_valor1.get()
        valor2 = entrada_valor2.get()

        resultado = float(valor1) + float(valor2)
        resultado_suma_var.set(f"El resultado de la suma es: {resultado}")

    except ValueError:
        resultado_suma_var.set("Ingresa valores numéricos.")

def on_enter_pressed(event):
    if ventana.focus_get() in (entrada_hora_inicio, entrada_hora_fin):
        calcular_diferencia()
    elif ventana.focus_get() in (entrada_valor1, entrada_valor2):
        sumar_valores()

def mostrar_creditos():
    ventana_creditos = tk.Toplevel(ventana)
    ventana_creditos.title("Créditos")

    # Obtiene las dimensiones de la pantalla
    ancho_pantalla = ventana_creditos.winfo_screenwidth()
    alto_pantalla = ventana_creditos.winfo_screenheight()

    # Calcula las coordenadas para centrar la ventana de créditos
    x = (ancho_pantalla - 300) // 2
    y = (alto_pantalla - 100) // 2

    # Posiciona la ventana de créditos en el centro de la pantalla
    

    ventana_creditos.geometry(f"300x100+{x}+{y}")  # Tamaño de la ventana de créditos
    mensaje = "Créditos del desarrollador: saturno2000"
    etiqueta_creditos = tk.Label(ventana_creditos, text=mensaje)
    etiqueta_creditos.pack()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Direnstalker")

# Obtiene las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcula las coordenadas para centrar la ventana principal
x = (ancho_pantalla - 260) // 2
y = (alto_pantalla - 250) // 2

# Posiciona la ventana principal en el centro de la pantalla
ventana.geometry(f"260x250+{x}+{y}")

# Etiquetas y campos de entrada para calcular la diferencia de horas
etiqueta_hora_inicio = tk.Label(ventana, text="Hora de inicio (HH:MM):", anchor="center")
entrada_hora_inicio = tk.Entry(ventana)
etiqueta_hora_fin = tk.Label(ventana, text="Hora de fin (HH:MM):", anchor="center")
entrada_hora_fin = tk.Entry(ventana)
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_diferencia)
resultado_var = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado_var, anchor="center")

# Etiquetas y campos de entrada para sumar valores
etiqueta_valor1 = tk.Label(ventana, text="Ingresa el primer valor:", anchor="center")
entrada_valor1 = tk.Entry(ventana)
etiqueta_valor2 = tk.Label(ventana, text="Ingresa el segundo valor:", anchor="center")
entrada_valor2 = tk.Entry(ventana)
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_valores)
resultado_suma_var = tk.StringVar()
etiqueta_resultado_suma = tk.Label(ventana, textvariable=resultado_suma_var, anchor="center")

# Botón para mostrar los créditos
boton_creditos = tk.Button(ventana, text="Créditos", command=mostrar_creditos)

# Coloca los elementos en la ventana
etiqueta_hora_inicio.grid(row=0, column=0, sticky="nsew")
entrada_hora_inicio.grid(row=0, column=1, sticky="nsew")
etiqueta_hora_fin.grid(row=1, column=0, sticky="nsew")
entrada_hora_fin.grid(row=1, column=1, sticky="nsew")
boton_calcular.grid(row=2, column=0, columnspan=2, sticky="nsew")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, sticky="nsew")

etiqueta_valor1.grid(row=4, column=0, sticky="nsew")
entrada_valor1.grid(row=4, column=1, sticky="nsew")
etiqueta_valor2.grid(row=5, column=0, sticky="nsew")
entrada_valor2.grid(row=5, column=1, sticky="nsew")
boton_sumar.grid(row=6, column=0, columnspan=2, sticky="nsew")
etiqueta_resultado_suma.grid(row=7, column=0, columnspan=2, sticky="nsew")

boton_creditos.grid(row=8, column=0, columnspan=2, sticky="nsew")

# Configura el grid para que los elementos se expandan
for i in range(9):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

# Asociar la tecla Enter a la función on_enter_pressed
ventana.bind('<Return>', on_enter_pressed)

# Inicia la aplicación
ventana.mainloop()
