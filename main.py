import tkinter as tk
press = True


# Crear una instancia de la clase Tk (raíz de la aplicación)
from PIL import Image, ImageTk


# Cargar la imagen y mantener una referencia
class tablero():

    casillas = []


    def __init__(self,root):
        self.root = root
        # Botón 1 con imagen redimensionada
        white_p = pieza_blanca(pb)
        black_p = pieza_negra(pn)

        #button1 = tk.Button(root, image=pb, command=lambda: white_p.opions(0, 2), bg="red", width=50, height=50)
        #button1.grid(row=0, column=0)
        #self.piezas_blancas.append(button1)

        # Botón 2 y Botón 3 sn imagen
        for i in range(0, 8):
            array_c = []
            for j in range(0, 8):
                if i==1:
                    button = tk.Button(root, image=pb, command= lambda column=j : white_p.pyimage1(column, 1, 2), bg="red", width=50, height=50)
                    array_c.append(button)
                    button.grid(row=1, column=j)

                elif i==6:
                    button = tk.Button(root, image=pn, command=lambda column=j: black_p.pyimage8(column, 6, -2), bg="red", width=50, height=50)
                    array_c.append(button)
                    button.grid(row=6, column=j)
                else:
                    button = tk.Button(root, image=default, bg="red", width=50, height=50)
                    array_c.append(button)
                    button.grid(row=i, column=j)
            self.casillas.append(array_c)


        """PIEZAS BLANCAS"""
        white_tr = pieza_blanca(tb)
        self.casillas[0][0].config(image=tb, command=lambda : white_tr.pyimage3(0, 0))
        self.casillas[0][1].config(image=ab)
        self.casillas[0][2].config(image=cb)
        self.casillas[0][3].config(image=rb)
        self.casillas[0][-4].config(image=qb)
        self.casillas[0][-3].config(image=cb)
        self.casillas[0][-2].config(image=ab)
        self.casillas[0][-1].config(image=tb)
        """PIEZAS NEGRAS"""
        self.casillas[7][0].config(image=tn)
        self.casillas[7][1].config(image=an)
        self.casillas[7][2].config(image=cn)
        self.casillas[7][3].config(image=rn)
        self.casillas[7][-4].config(image=qn)
        self.casillas[7][-3].config(image=cn)
        self.casillas[7][-2].config(image=an)
        self.casillas[7][-1].config(image=tn)
        #button2 = tk.Button(root, image=pn, command=lambda: black_p.opions(8,-2), bg="red", width=50, height=50)
        #button2.grid(row=8, column=0)
        #self.piezas_blancas.append(button2)


sw_w=True
sw_b=False
class pieza_blanca:
    piezas_blancas = ["pyimage1", "pyimage3", "pyimage4", "pyimage5", "pyimage6", "pyimage7"]
    piezas_negras = ["pyimage8", "pyimage9", "pyimage10", "pyimage11", "pyimage12", "pyimage13"]

    step = 1
    def __init__(self,imagen_pieza):
        self.imagen_pieza= imagen_pieza
        pass
    def back_to_normal(self):
        global sw_w,sw_b
        for i in range(0,8):

            for k in tablero.casillas[i]:
                imagen_ = dict(k.config())["image"][-1]
                if dict(k.config())["background"][-1] !="red":
                    k.config(bg ="red")

                    if str(imagen_) =="pyimage1":
                        objeto_1 = pieza_blanca(pb)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_1.pyimage1(column,row,1))
                    elif str(imagen_) =="pyimage8":
                        objeto_2 = pieza_negra(pn)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k): objeto_2.pyimage8(column,row,-1))
                    elif str(imagen_) =="pyimage3":
                        objeto_3 = pieza_blanca(tb)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_3.pyimage3(column,row))
                    else:
                        k.config(command = "")

    def pyimage3(self, column, first_square):
        global sw_w, sw_b
        assert sw_w == True
        self.back_to_normal()

        imagen_ =  dict(tablero.casillas[first_square][column].config())["image"][-1]
        print(imagen_)
        #Derecha
        try:
            for i in range(column+1,8):
                imagen_2 = dict(tablero.casillas[first_square][i].config())["image"][-1]
                if imagen_2 !="pyimage2" :
                    if imagen_2 not in self.piezas_blancas:
                            tablero.casillas[first_square][i].config(bg="purple",
                                                                 command=lambda last_column=i: self.mover(first_square,
                                                                                                          column,
                                                                                                          last_column,
                                                                                                          first_square, 8,
                                                                                                          imagen_))
                    break

                tablero.casillas[first_square][i].config(bg="blue",command=lambda last_column=i: self.mover(first_square, column,last_column,first_square, 8,imagen_))
        except:
            pass
        #Izquierda
        try:
            for k in range(column-1, -1,-1):
                imagen_3 = dict(tablero.casillas[first_square][k].config())["image"][-1]
                if imagen_3 != "pyimage2":
                    if imagen_3 not in self.piezas_blancas:
                        tablero.casillas[first_square][k].config(bg="purple",
                                                             command=lambda last_column=k: self.mover(first_square,
                                                                                                      column,
                                                                                                      last_column,
                                                                                                      first_square, 8,
                                                                                                      imagen_))
                    break

                tablero.casillas[first_square][k].config(bg="blue",
                                                                  command=lambda last_column=k: self.mover(
                                                                      first_square, column,
                                                                      last_column, first_square,
                                                                      8, imagen_))
        except:
            pass
                #arriba
        try:
            for j in range(first_square+1,8):
                imagen_4 = dict(tablero.casillas[j][column].config())["image"][-1]
                if imagen_4 != "pyimage2":
                    if imagen_4 not in self.piezas_blancas:
                        tablero.casillas[j][column].config(bg="purple",
                                                             command=lambda last_square=j: self.mover(first_square,
                                                                                                      column,
                                                                                                      column,
                                                                                                      last_square, 8,
                                                                                                      imagen_))
                    break
                tablero.casillas[j][column].config(bg="blue", command=lambda last_square=j: self.mover(first_square, column,column, last_square, 8,imagen_))
        except:
            pass
        #abajo
        try:
            for l in range(first_square-1, -1,-1):
                imagen_5 = dict(tablero.casillas[l][column].config())["image"][-1]
                if imagen_5 != "pyimage2":
                    if imagen_5 not in self.piezas_blancas:
                        tablero.casillas[l][column].config(bg="purple",
                                                             command=lambda last_square=l: self.mover(first_square,
                                                                                                      column,
                                                                                                      column,
                                                                                                      last_square, 8,
                                                                                                      imagen_))
                    break
                tablero.casillas[l][column].config(bg="blue",
                                                   command=lambda last_square=l: self.mover(first_square, column, column,
                                                                                            last_square, 8, imagen_))
        except:
            pass
    """def asesinar(self,first_square,column,last_column,row,lenght):
        self.back_to_normal()

        global sw_w,sw_b


        tablero.casillas[row][last_column].config(image=self.imagen_pieza, bg="red", command = lambda: self.pyimage1(last_column, row, lenght))
        tablero.casillas[first_square][column].config(image=default, command="")
        for j in range(first_square + self.step, first_square + self.step + lenght, self.step):
            tablero.casillas[j][column].config(bg="red")
            tablero.casillas[j][column].config(command="")
        sw_b = True
        sw_w = False"""
    def pyimage1(self, column, first_square, movimiento=1):
        global sw_w, sw_b
        assert sw_w == True

        self.back_to_normal()
        try:
            if dict(tablero.casillas[first_square+1][column+1].config())["image"][-1]!="pyimage2":
                tablero.casillas[first_square+1][column+1].config(bg ="purple", command= lambda row=first_square+1,last_column=column+1: self.mover(first_square,column,last_column ,row,movimiento,pb))


        except:
            pass
        try:
            if dict(tablero.casillas[first_square + 1][column - 1].config())["image"][-1] != "pyimage2" :
                tablero.casillas[first_square + 1][column - 1].config(bg="purple", command=lambda row=first_square + 1,
                                                                                                  last_column=column - 1: self.mover(
                    first_square, column, last_column, row, movimiento,pb))
        except:
            pass
        for i in range(first_square+self.step,first_square+self.step+movimiento,self.step):
            configuracion = tablero.casillas[i][column].config()
            if dict(configuracion)["image"][-1] !="pyimage2":
                break

            tablero.casillas[i][column].config(bg ="blue", command= lambda row=i: self.mover(first_square,column,column, row, movimiento-1,pb))

    def mover(self,first_square,column,last_column,last_square,lenght,pieza):

        global sw_w, sw_b
        function_name = str(pieza)
        #func =getattr(self,function_name,None)

        tablero.casillas[last_square][last_column].config(image=pieza)
        tablero.casillas[first_square][column].config(image=default, command="")
        self.back_to_normal()
        #tablero.casillas[last_square][last_column].config(command = lambda : func(last_column, last_square))
        sw_b =True
        sw_w = False



class pieza_negra(pieza_blanca):
    step = -1

    def pyimage8(self, column, first_square, movimiento=-1):
        global sw_w, sw_b,pieza_seleccionada_negra
        assert sw_b == True
        objetoo = pieza_blanca(pb)
        objetoo.back_to_normal()
        try:
            if dict(tablero.casillas[first_square - 1][column - 1].config())["image"][-1] != "pyimage2" :
                tablero.casillas[first_square - 1][column - 1].config(bg="purple", command=lambda last_square=first_square-1,last_column=column -1: self.mover(
                    first_square, column, column-1, first_square-1, movimiento,pn))
        except:
            pass
        try:
            if dict(tablero.casillas[first_square - 1][column + 1].config())["image"][-1] != "pyimage2":
                tablero.casillas[first_square - 1][column + 1].config(bg="purple", command=lambda row=first_square-1,last_column=column+1: self.mover(
                    first_square, column, column+1, first_square-1, movimiento,pn))
        except:
            pass

        for i in range(first_square+self.step,first_square+self.step+movimiento,self.step):
            configuracion = tablero.casillas[i][column].config()
            if dict(configuracion)["image"][-1] != "pyimage2":

                break

            tablero.casillas[i][column].config(bg ="blue", command= lambda row=i: self.mover(first_square,column,column, row, movimiento+1,pn))



    """def asesinar(self,first_square,column,last_column,row,lenght):
        super().asesinar(first_square,column,last_column,row,lenght)
        global sw_w, sw_b
        sw_w = True
        sw_b = False"""

    def mover(self,first_square,column,last_column,last_square,lenght,pieza):
        super().mover(first_square, column,last_column, last_square, lenght,pieza)

        global sw_w, sw_b
        sw_w = True
        sw_b = False
        self.back_to_normal()





if __name__ == "__main__":
    root = tk.Tk()
    img = Image.open("images/peon-blanco.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    pb = ImageTk.PhotoImage(img)
    img_2 = Image.open("images/nada.png")
    img_2 = img_2.resize((50, 50), Image.ANTIALIAS)
    default = ImageTk.PhotoImage(img_2)
    img = Image.open("images/torre-blanca.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    tb = ImageTk.PhotoImage(img)
    img = Image.open("images/alfil-blanco.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    ab= ImageTk.PhotoImage(img)
    img = Image.open("images/caballo-blanco.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    cb = ImageTk.PhotoImage(img)
    img = Image.open("images/rey-blanco.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    rb = ImageTk.PhotoImage(img)
    img = Image.open("images/reina-blanca.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    qb = ImageTk.PhotoImage(img)


    """PIEZAS NEGRAS"""
    img = Image.open("images/peon-negro.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    pn = ImageTk.PhotoImage(img)
    img = Image.open("images/torre-negra.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    tn = ImageTk.PhotoImage(img)
    img = Image.open("images/alfil-negro.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    an = ImageTk.PhotoImage(img)
    img = Image.open("images/caballo-negro.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    cn = ImageTk.PhotoImage(img)
    img = Image.open("images/rey-negro.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    rn = ImageTk.PhotoImage(img)
    img = Image.open("images/reina-negra.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    qn = ImageTk.PhotoImage(img)

    tablero_ajedrez = tablero(root)


    root.mainloop()
