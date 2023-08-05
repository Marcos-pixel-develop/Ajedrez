import tkinter as tk
press = True


# Crear una instancia de la clase Tk (raíz de la aplicación)
from PIL import Image, ImageTk

sw_w=True
sw_b=False
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
        white_al = pieza_blanca(ab)
        white_cb = pieza_blanca(cb)
        white_qn = pieza_blanca(qb)
        white_re = pieza_blanca(rb)
        black_qn = pieza_negra(qn)
        black_re = pieza_negra(rn)
        black_cb = pieza_negra(cn)
        black_tr = pieza_negra(tn)
        black_al = pieza_negra(an)


        self.casillas[0][0].config(image=tb, command=lambda : white_tr.pyimage3(0, 0))
        self.casillas[0][1].config(image=cb,command=lambda : white_cb.pyimage5(1,0))
        self.casillas[0][2].config(image=ab, command = lambda : white_al.pyimage4(2,0))
        self.casillas[0][3].config(image=rb, command = lambda : white_re.rey(3,0))
        self.casillas[0][-4].config(image=qb, command= lambda :white_qn.pyimage7(4,0))
        self.casillas[0][-3].config(image=ab, command = lambda : white_al.pyimage4(5,0))
        self.casillas[0][-2].config(image=cb, command = lambda : white_cb.pyimage5(6,0))
        self.casillas[0][-1].config(image=tb,  command=lambda : white_tr.pyimage3(7, 0))
        """PIEZAS NEGRAS"""
        self.casillas[7][0].config(image=tn, command=lambda : black_tr.pyimage3(0, 7))
        self.casillas[7][1].config(image=cn, command= lambda : black_cb.pyimage5(1,7))
        self.casillas[7][2].config(image=an,command = lambda : black_al.pyimage4(2,7))
        self.casillas[7][3].config(image=rn,command = lambda: black_re.rey(3,7))
        self.casillas[7][-4].config(image=qn, command=lambda :black_qn.pyimage7(4,7))
        self.casillas[7][-3].config(image=an, command=lambda: black_al.pyimage4(5, 7))
        self.casillas[7][-2].config(image=cn, command=lambda :black_cb.pyimage5(6,7))
        self.casillas[7][-1].config(image=tn, command=lambda : black_al.pyimage3(7, 7))
        #button2 = tk.Button(root, image=pn, command=lambda: black_p.opions(8,-2), bg="red", width=50, height=50)
        #button2.grid(row=8, column=0)
        #self.piezas_blancas.append(button2)


fila_r= 0
column_r=3
class pieza_blanca:
    piezas = ["pyimage1", "pyimage3", "pyimage4", "pyimage5", "pyimage6", "pyimage7"]

    step = 1
    def __init__(self,imagen_pieza):
        global fila_r, column_r
        self.imagen_pieza= imagen_pieza



    def back_to_normal(self):
        global fila_r,column_r







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
                    elif str(imagen_) =="pyimage9":
                        objeto_3 = pieza_negra(tn)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k): objeto_3.pyimage3(column,row))
                    elif str(imagen_) =="pyimage3":
                        objeto_4 = pieza_blanca(tb)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_4.pyimage3(column,row))
                    elif str(imagen_) =="pyimage4":
                        objeto_5 = pieza_blanca(ab)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_5.pyimage4(column,row))
                    elif str(imagen_) =="pyimage10":
                        objeto_6 = pieza_negra(an)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_6.pyimage4(column,row))
                    elif str(imagen_) =="pyimage5":
                        objeto_7 = pieza_blanca(cb)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_7.pyimage5(column,row))
                    elif str(imagen_) =="pyimage11":
                        objeto_8 = pieza_negra(cn)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_8.pyimage5(column,row))
                    elif str(imagen_) =="pyimage13":
                        objeto_9 = pieza_negra(qn)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_9.pyimage7(column,row))
                    elif str(imagen_) =="pyimage7":
                        objeto_10 = pieza_blanca(qn)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_10.pyimage7(column,row))
                    elif str(imagen_) =="pyimage6":
                        objeto_11 = pieza_blanca(rb)
                        k.config(command=lambda row = i, column = tablero.casillas[i].index(k) :objeto_11.rey(column,row))
                    elif str(imagen_) == "pyimage12":
                        objeto_12 = pieza_negra(rn)
                        k.config(command=lambda row=i, column=tablero.casillas[i].index(k): objeto_12.rey(column, row))
                    else:
                        k.config(command = "")
        first_square = fila_r
        column = column_r
        imagen_rey = dict(tablero.casillas[0][3].config())["image"][-1]
        # verificar casillas
        for u in range(3):
            for j in range(3):
                if first_square - 1 + u <= 7 and column - 1 + j <= 7 and first_square - 1 + u >= 0 and column - 1 + j >= 0:
                    imagen_ = dict(tablero.casillas[first_square - 1 + u][column - 1 + j].config())["image"][-1]
                    if imagen_ != imagen_rey and first_square - 1 + u >= 0 and column - 1 + j >= 0:
                        if imagen_ == "pyimage2":
                            tablero.casillas[first_square - 1 + u][column - 1 + j].config(command= lambda last_square= first_square - 1 + u, last_column=column - 1 + j: self.mover(first_square,column,last_column,last_square,8,imagen))


    def decorator(self):
        pass
    def pyimage5(self,column,first_square):
        global sw_w, sw_b
        assert sw_w == True
        self.back_to_normal()
        imagen_ =  dict(tablero.casillas[first_square][column].config())["image"][-1]
        lista = [2, -2]
        color = "blue"
        for i in range(2):
            value = first_square + lista[i]
            value_2 = column + lista[i]

            if value>=0:
                if column+1>=0:
                    try:
                        if dict(tablero.casillas[value][column + 1].config())["image"][-1] !="pyimage2":
                            color = "purple"

                        if dict(tablero.casillas[value][column + 1].config())["image"][-1] not in self.piezas:
                            tablero.casillas[value][column + 1].config(bg=color,command = lambda last_column=column+1,last_square=value :self.mover(first_square,column,last_column,last_square,8,imagen_))
                        color = "blue"
                    except:
                        pass
                if column-1>=0:
                    try:
                        if dict(tablero.casillas[value][column - 1].config())["image"][-1] !="pyimage2":
                            color = "purple"
                        if dict(tablero.casillas[value][column - 1].config())["image"][-1] not in self.piezas:
                            tablero.casillas[value][column - 1].config(bg=color, command= lambda last_column =column-1, last_square=value: self.mover(first_square,column,last_column,last_square,8,imagen_))
                        color = "blue"
                    except:
                        pass
            if value_2>=0:
                if first_square +1 >=0:
                    try:
                        if dict(tablero.casillas[first_square+1][value_2].config())["image"][-1] !="pyimage2" :
                            color = "purple"
                        if dict(tablero.casillas[first_square+1][value_2].config())["image"][-1] not in self.piezas:
                            tablero.casillas[first_square + 1][value_2].config(bg=color, command= lambda last_column=value_2,last_square=first_square+1:self.mover(first_square,column,last_column,last_square,8,imagen_))
                        color = "blue"
                    except:
                        pass
                if first_square-1 >=0 :
                    try:

                        if dict(tablero.casillas[first_square-1][value_2].config())["image"][-1] !="pyimage2":
                            color = "purple"
                        if dict(tablero.casillas[first_square-1][value_2].config())["image"][-1] not in self.piezas:
                            tablero.casillas[first_square -1][value_2].config(bg=color, command= lambda last_column=value_2,last_square=first_square-1:self.mover(first_square,column,last_column,last_square,8,imagen_))
                        color = "blue"
                    except:
                        pass
    pass
    def pyimage4(self,column,first_square):
        global sw_w, sw_b
        assert sw_w == True
        start = 1
        self.back_to_normal()
        imagen_ =  dict(tablero.casillas[first_square][column].config())["image"][-1]
        try:
            for i in range(first_square+1,8):

                imagen_2 = dict(tablero.casillas[i][column+i-first_square].config())["image"][-1]
                if imagen_2 !="pyimage2" :
                    if imagen_2 not in self.piezas:
                            tablero.casillas[i][column+i-first_square].config(bg="purple",
                                                                 command=lambda last_square=i ,last_column=column+i-first_square: self.mover(first_square,
                                                                                                          column,
                                                                                                          last_column,
                                                                                                          last_square, 8,
                                                                                                          imagen_))
                    break

                tablero.casillas[i][column+i-first_square].config(bg="blue",command=lambda last_square=i,last_column=column+i-first_square: self.mover(first_square, column,last_column,last_square, 8,imagen_))
        except:
            pass
        #Izquierda
        try:
            for k in range(first_square+1,8):
                imagen_3 = dict(tablero.casillas[k][column-k+first_square].config())["image"][-1]
                if imagen_3 != "pyimage2":
                    if imagen_3 not in self.piezas and column-k+first_square>=0:
                        tablero.casillas[k][column-k+first_square].config(bg="purple",
                                                             command=lambda last_square = k,last_column=column-k+first_square: self.mover(first_square,
                                                                                                      column,
                                                                                                      last_column,
                                                                                                      last_square, 8,
                                                                                                      imagen_))
                    break
                if column-k+first_square<0:
                    break
                tablero.casillas[k][column-k+first_square].config(bg="blue",
                                                                  command=lambda last_square = k,last_column=column-k+first_square: self.mover(
                                                                      first_square, column,
                                                                      last_column, last_square,
                                                                      8, imagen_))
        except:
            pass
                #arriba

        try:
            for j in range(1,first_square+1):
                imagen_4 = dict(tablero.casillas[first_square-j][column+j].config())["image"][-1]
                if imagen_4 != "pyimage2":
                    if imagen_4 not in self.piezas:
                        tablero.casillas[first_square-j][column+j].config(bg="purple",
                                                             command=lambda last_column=column+j,last_square=first_square-j: self.mover(first_square,
                                                                                                      column,
                                                                                                      last_column,
                                                                                                      last_square, 8,
                                                                                                      imagen_))
                    break
                tablero.casillas[first_square-j][column+j].config(bg="blue", command=lambda last_column = column+j , last_square=first_square-j: self.mover(first_square, column,last_column, last_square, 8,imagen_))
        except:
            pass
        #abajo
        try:
            for l in range(1,first_square+1):
                imagen_5 = dict(tablero.casillas[first_square-l][column-l].config())["image"][-1]
                if imagen_5 != "pyimage2":
                    print(column-l)
                    if imagen_5 not in self.piezas and column-l>-1:
                        print(column - l)

                        tablero.casillas[first_square-l][column-l].config(bg="purple",
                                                             command=lambda last_column=column-l,last_square=first_square-l: self.mover(first_square,
                                                                                                      column,
                                                                                                      last_column,
                                                                                                      last_square, 8,
                                                                                                      imagen_))
                    break
                if column-l<0:
                    break
                tablero.casillas[first_square-l][column-l].config(bg="blue",
                                                   command=lambda last_column = column-l,last_square=first_square-l: self.mover(first_square, column, last_column,
                                                                                            last_square, 8, imagen_))
        except:
            pass

    def pyimage3(self, column, first_square):
        global sw_w, sw_b
        assert sw_w == True
        dist_column = 8
        if str(self.imagen_pieza) =="pyimage7" or str(self.imagen_pieza) =="pyimage13":
            pass
        else:
            self.back_to_normal()
        imagen_ =  dict(tablero.casillas[first_square][column].config())["image"][-1]
        #Derecha
        try:
            for i in range(column+1,8):
                imagen_2 = dict(tablero.casillas[first_square][i].config())["image"][-1]
                if imagen_2 !="pyimage2" :
                    if imagen_2 not in self.piezas:
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
                    if imagen_3 not in self.piezas:
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
                    if imagen_4 not in self.piezas:
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
                    if imagen_5 not in self.piezas:
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
            imagen = dict(tablero.casillas[first_square+1][column+1].config())["image"][-1]
            if dict(tablero.casillas[first_square+1][column+1].config())["image"][-1]!="pyimage2" and str(imagen) not in self.piezas:
                tablero.casillas[first_square+1][column+1].config(bg ="purple", command= lambda row=first_square+1,last_column=column+1: self.mover(first_square,column,last_column ,row,movimiento,pb))


        except:
            pass
        try:
            imagen = dict(tablero.casillas[first_square+1][column-1].config())["image"][-1]

            if dict(tablero.casillas[first_square + 1][column - 1].config())["image"][-1] != "pyimage2" and str(imagen) not in self.piezas:
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

    def rey(self, column, first_square):
        global sw_w,sw_b
        assert  sw_w == True
        self.back_to_normal()
        imagen = dict(tablero.casillas[first_square][column].config())["image"][-1]
        print(imagen)
        for i in range(3):
            for j in range(3):
                if first_square-1+i<=7 and column-1+j<=7:
                    imagen_ = dict(tablero.casillas[first_square-1+i][column-1+j].config())["image"][-1]
                    if imagen_ !=imagen and first_square-1+i>=0 and  column-1+j>=0:
                        if imagen_ != "pyimage2" and imagen_ not in self.piezas:
                            tablero.casillas[first_square - 1 + i][column - 1 + j].config(bg="purple",
                                                                                          command=lambda
                                                                                              last_square=first_square - 1 + i,
                                                                                              last_column=column - 1 + j: self.mover(
                                                                                              first_square, column, last_column,
                                                                                              last_square,
                                                                                              8, imagen))
                        elif imagen_ == "pyimage2":
                            tablero.casillas[first_square-1+i][column-1+j].config(bg="blue",
                                                               command=lambda last_square=first_square-1+i,last_column=column-1+j: self.mover(first_square, column, last_column,last_square,
                                                                                                8, imagen))

    def pyimage7(self,column,first_square):
        global sw_w, sw_b
        assert sw_w == True

        self.pyimage4(column,first_square)
        print("........")
        self.pyimage3(column,first_square)


    def mover(self,first_square,column,last_column,last_square,lenght,pieza):

        global sw_w, sw_b
        #func =getattr(self,function_name,None)

        tablero.casillas[last_square][last_column].config(image=pieza)
        tablero.casillas[first_square][column].config(image=default, command="")
        self.back_to_normal()
        #tablero.casillas[last_square][last_column].config(command = lambda : func(last_column, last_square))
        sw_b =True
        sw_w = False



class pieza_negra(pieza_blanca):
    step = -1
    piezas = ["pyimage8", "pyimage9", "pyimage10", "pyimage11", "pyimage12", "pyimage13"]
    def pyimage7(self,column,first_square):
        global sw_w, sw_b
        assert sw_b == True
        sw_w = True
        super().pyimage7(column, first_square)
        sw_w = False


    def pyimage5(self,column,first_square):
        global sw_w, sw_b

        assert sw_b == True
        sw_w = True
        super().pyimage5(column, first_square)
        sw_w = False



    def rey(self,column,first_square):
        global sw_w, sw_b
        assert sw_b == True
        sw_w = True
        super().rey(column, first_square)
        sw_w = False

    def pyimage3(self, column, first_square):
        global sw_w , sw_b
        assert sw_b ==True
        sw_w = True
        super().pyimage3(column,first_square)
        sw_w = False

    def pyimage4(self, column, first_square):
        global sw_w , sw_b
        assert sw_b ==True
        sw_w = True
        super().pyimage4(column,first_square)
        sw_w = False

    def pyimage8(self, column, first_square, movimiento=-1):
        global sw_w, sw_b,pieza_seleccionada_negra
        assert sw_b == True
        objetoo = pieza_blanca(pb)
        objetoo.back_to_normal()
        try:
            imagen = dict(tablero.casillas[first_square-1][column-1].config())["image"][-1]

            if dict(tablero.casillas[first_square - 1][column - 1].config())["image"][-1] != "pyimage2" and str(imagen)  not in self.piezas:
                tablero.casillas[first_square - 1][column - 1].config(bg="purple", command=lambda last_square=first_square-1,last_column=column -1: self.mover(
                    first_square, column, column-1, first_square-1, movimiento,pn))
        except:
            pass
        try:
            imagen = dict(tablero.casillas[first_square+1][column+1].config())["image"][-1]

            if dict(tablero.casillas[first_square - 1][column + 1].config())["image"][-1] != "pyimage2"  and str(imagen)  not in self.piezas:
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
