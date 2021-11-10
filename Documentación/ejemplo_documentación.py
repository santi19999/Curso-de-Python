class Areas:
    
    def areaCuadrado(lado):
        '''Calcula el área de un cuadrado
        elevando al cuadrado el lado pasado por parámetro'''
        return "El area del cuadrado es : " + str(lado*lado)

    def areaTriangulo(base,altura):
        '''Calcula el área del Triángulo utilizando los parámetros base y altura'''
        return "El area del triágulo es : " + str((base*altura)/2)


help(Areas.areaTriangulo)