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
        white_p = pieza_blanca(pb)
        black_p = pieza_negra(pn)
        # Botón 1 con imagen redimensionada
        button1 = tk.Button(root, image=pb, command=lambda: white_p.opions(0, 2), bg="red", width=50, height=50)
        button1.grid(row=0, column=0)
        self.piezas_blancas.append(button1)

        # Botón 2 y Botón 3 sn imagen
        for i in range(1, 8):
            button = tk.Button(root, image=default, bg="red", width=50, height=50)
            self.piezas_blancas.append(button)
            button.grid(row=i, column=0)

        button2 = tk.Button(root, image=pn, command=lambda: black_p.opions(8,-2), bg="red", width=50, height=50)
        button2.grid(row=8, column=0)
        self.piezas_blancas.append(button2)


sw_w=True
sw_b=False
class pieza_blanca:
    option= []
    step = 1
    def __init__(self,imagen_pieza):
        self.imagen_pieza= imagen_pieza
        pass
    def opions(self,first_square,movimiento):
        global sw_w, sw_b

        assert sw_w == True

        for i in range(first_square+self.step,first_square+self.step+movimiento,self.step):
            configuracion = tablero.piezas_blancas[i].config()
            if dict(configuracion)["image"][-1] !="pyimage2":
                break

            tablero.piezas_blancas[i].config(bg = "blue",command= lambda row=i: self.mover(first_square,row,movimiento))

    def mover(self,first_square,last_square,lenght):
        global sw_w, sw_b

        tablero.piezas_blancas[last_square].config(image=self.imagen_pieza)
        tablero.piezas_blancas[first_square].config(image=default, command="")
        for j in range(first_square+self.step,first_square+self.step+lenght,self.step):
            tablero.piezas_blancas[j].config(bg="red")
            tablero.piezas_blancas[j].config(command="")
        tablero.piezas_blancas[last_square].config(command = lambda: self.opions(last_square,lenght))
        sw_b =True
        sw_w = False

class pieza_negra(pieza_blanca):
    step = -1
    def opions(self,first_square,movimiento):
        global sw_w, sw_b
        assert sw_b == True , f''
        for i in range(first_square+self.step,first_square+self.step+movimiento,self.step):
            configuracion = tablero.piezas_blancas[i].config()
            if dict(configuracion)["image"][-1] != "pyimage2":
                break

            tablero.piezas_blancas[i].config(bg = "blue",command= lambda row=i: self.mover(first_square,row,movimiento))
    def mover(self,first_square,last_square,lenght):
        super().mover(first_square,last_square,lenght)
        global sw_w,sw_b
        sw_w = True
        sw_b = False




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
