def pyimage3(self, column, first_square,color="blue"):
    global sw_w, sw_b
    assert sw_w == True
    if str(self.imagen_pieza) == "pyimage7" or str(self.imagen_pieza) == "pyimage13":
        pass
    else:
        self.back_to_normal()
    imagen_ = dict(tablero.casillas[first_square][column].config())["image"][-1]
    # Derecha
    try:
        for i in range(column + 1, 8):
            imagen_2 = dict(tablero.casillas[first_square][i].config())["image"][-1]
            if imagen_2 != "pyimage2":
                if imagen_2 not in self.piezas:
                    if color != "blue":
                        tablero.casillas[first_square][i].config(bg="green")
                    else:
                        tablero.casillas[first_square][i].config(bg="purple",
                                                             command=lambda last_column=i: self.mover(first_square,
                                                                                                      column,
                                                                                                      last_column,
                                                                                                      first_square, 8,
                                                                                                      imagen_))
                break
            if color=="blue":
                tablero.casillas[first_square][i].config(bg="blue",
                                                     command=lambda last_column=i: self.mover(first_square, column,
                                                                                              last_column, first_square,
                                                                                              8, imagen_))
    except:
        pass
    # Izquierda
    try:
        for k in range(column - 1, -1, -1):
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
        # arriba
    try:
        for j in range(first_square + 1, 8):
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
            tablero.casillas[j][column].config(bg="blue",
                                               command=lambda last_square=j: self.mover(first_square, column, column,
                                                                                        last_square, 8, imagen_))
    except:
        pass
    # abajo
    try:
        for l in range(first_square - 1, -1, -1):
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