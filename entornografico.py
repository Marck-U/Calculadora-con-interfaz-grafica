from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk, font  # Carga ttk (para widgets nuevos 8.5+)
import getpass

class Aplication():
    def __init__(self):
        self.raiz = Tk()

        # Define la dimensión de la ventana
        self.raiz.geometry("430x200")
        # Se establece que no se pueda modificar el tamaño de la ventana
        self.raiz.resizable(0,0)
        self.raiz.title("Calculadora")
        # cambia el formato de la fuente actual a negrita
        self.fuente = font.Font(weight='bold')
        # Se definen las etiquetas  que irán con el textbox y se le aplica la fuente importada
        self.etiq1 = ttk.Label(self.raiz, text="numero 1:", font=self.fuente)
        self.etiq2 = ttk.Label(self.raiz, text="numero 2:", font=self.fuente)

        self.mensaje = StringVar()
        self.etiq3 = ttk.Label(self.raiz, textvariable=self.mensaje, font=self.fuente, foreground='blue')

        # Se declaran dos variables de tipo numerico
        self.numero1 = IntVar()
        self.numero2 = IntVar()

        # Se declaran dos texbox
        self.txt_numero1 = ttk.Entry(
        self.raiz, textvariable=self.numero1, width=30)
        self.txt_numero2 = ttk.Entry(
        self.raiz, textvariable=self.numero2, width=30)
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)

        # Se declaran los botones
        self.boton1 = ttk.Button(self.raiz, text="Sumar", command=self.sumar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", command=quit)
        self.boton3 = ttk.Button(self.raiz, text="Restar", command=self.restar)
        self.boton4 = ttk.Button(self.raiz, text="Multiplicar", command=self.multiplicar)
        self.boton5 = ttk.Button(self.raiz, text="Dividir", command=self.dividir)

        # Se definen las posiciones de los txt, separador, label y botones
        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=200, y=120)
        self.txt_numero1.place(x=150, y=42)
        self.txt_numero2.place(x=150, y=82)
        self.separ1.place(x=5, y=170, bordermode=OUTSIDE,height=10, width=420)
        self.boton1.place(x=310, y=110)
        self.boton2.place(x=310, y=140)
        self.boton3.place(x=220, y=110)
        self.boton4.place(x=130, y=110)
        self.boton5.place(x=40, y=110)
        self.txt_numero1.focus_set()
        self.raiz.mainloop()
    # Se definen los metodos para las distintas funciones de aritmetica

    def sumar(self):
        resultado = self.numero1.get() + self.numero2.get()
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado)) 

    def restar(self):
        resultado = self.numero1.get() - self.numero2.get()
        print(resultado)
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado))

    def multiplicar(self):
        resultado = self.numero1.get() * self.numero2.get()
        print(resultado)
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado))

    def dividir(self):
        resultado = self.numero1.get() / self.numero2.get()
        print(resultado)
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado))

def main():
    mi_app = Aplication()
    return 0

if __name__ == '__main__':
    main()
