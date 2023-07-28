import tkinter as tk
press = True


# Crear una instancia de la clase Tk (raíz de la aplicación)
from PIL import Image, ImageTk

# Cargar la imagen y mantener una referencia


class tablero():
    piezas_blancas = []
    piezas_negras = []
    def __init__(self,root):
        self.root = root
        white_p = pieza_blanca()
        black_p = pieza_negra()
        # Botón 1 con imagen redimensionada
        button1 = tk.Button(root, image=pb, command=lambda: white_p.opions(0, 1), bg="red", width=50, height=50)
        button1.grid(row=0, column=0)
        self.piezas_blancas.append(button1)

        # Botón 2 y Botón 3 sn imagen
        for i in range(1, 8):
            button = tk.Button(root, image=default, bg="red", width=50, height=50)
            self.piezas_blancas.append(button)

            button.grid(row=i, column=0)

        button2 = tk.Button(root, image=pn, command=lambda: black_p.opions(8,-1), bg="red", width=50, height=50)
        button2.grid(row=8, column=0)
        self.piezas_blancas.append(button2)



class pieza_blanca:
    option= []
    step = 1
    def __init__(self):
        pass
    def opions(self,first_square,movimiento):
        for i in range(first_square+self.step,first_square+self.step+movimiento,self.step):
            tablero.piezas_blancas[i].config(bg = "blue",command= lambda row=i: self.mover(first_square,row,movimiento))

    def mover(self,first_square,last_square,lenght):
        tablero.piezas_blancas[last_square].config(image=pb)
        tablero.piezas_blancas[first_square].config(image=default, command="")
        for j in range(first_square+1,first_square+1+lenght):
            tablero.piezas_blancas[j].config(bg="red")
            tablero.piezas_blancas[j].config(command="")
        tablero.piezas_blancas[last_square].config(command = lambda: self.opions(last_square,lenght))


class pieza_negra(pieza_blanca):
    step = -1
    pass

if __name__ == "__main__":
    root = tk.Tk()
    img = Image.open("images/peon-blanco.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    pb = ImageTk.PhotoImage(img)
    img_2 = Image.open("images/nada.png")
    img_2 = img_2.resize((50, 50), Image.ANTIALIAS)
    default = ImageTk.PhotoImage(img_2)
    img = Image.open("images/peon-negro.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    pn = ImageTk.PhotoImage(img)

    tablero_ajedrez = tablero(root)
    root.mainloop()
